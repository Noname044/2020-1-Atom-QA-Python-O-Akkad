from urllib import request
from urllib.parse import urljoin

import requests


class ResponseStatusCodeException(Exception):
    pass


class RequestErrorException(Exception):
    pass


class TargetClient:

    def __init__(self, email, password):
        self.base_url = 'https://target.my.com'

        self.session = requests.Session()

        self.email = email
        self.password = password
        self.login()

    def _request(self, method, location, status_code=200, allow_redir=True, headers=None, params=None, data=None,
                 json=True, jsonchik=None):
        url = urljoin(self.base_url, location)

        response = self.session.request(method, url, allow_redirects=allow_redir, headers=headers, params=params,
                                        data=data, json=jsonchik)

        if response.status_code != status_code:
            raise ResponseStatusCodeException(f' Got {response.status_code} {response.reason} for URL "{url}"')

        if json:
            json_response = response.json()

            if json_response.get('bStateError'):
                error = json_response['sErrorMsg']
                raise RequestErrorException(f'Request "{url}" dailed with error "{error}"!')
            return json_response
        return response

    def login(self):
        location = 'https://auth-ac.my.com/auth'

        headers = {
            'Referer': 'https://target.my.com/'
        }

        data = {
            'email': self.email,
            'password': self.password
        }
        self._request('POST', location, allow_redir=False, status_code=302, headers=headers, data=data, json=False)
        self.get_csrf()

    def get_csrf(self):
        location = 'https://target.my.com/csrf'

        headers = {
            'Referer': 'https://target.my.com/',
            'Origin': 'target.my.com'
        }
        self._request('GET', location, status_code=200, headers=headers, json=False)

    def post_audit(self, name, logic_type="or"):
        location = 'api/v2/remarketing/segments.json?fields=relations__object_type,relations__object_id,' \
                   'relations__params,relations_count,id,name,pass_condition,created,campaign_ids,users,flags'

        header = {
            'Referer': 'https://target.my.com/segments/segments_list/new',
            'X-CSRFToken': self.session.cookies['csrftoken']
        }

        data = {
            'name': name,
            'pass_condition': '1',
            'relations': [
                {
                    'object_type': 'remarketing_users_list',
                    'params': {
                        'source_id': '9912270',
                        'type': 'positive'
                    }
                }
            ],
            'logicType': logic_type
        }

        response = self._request('POST', location, headers=header, jsonchik=data)
        return response

    def delete_audit(self, id):
        location = f'https://target.my.com/api/v2/remarketing/segments/{id}.json'

        header = {
            'Referer': 'https://target.my.com/segments/segments_list',
            'X-CSRFToken': self.session.cookies['csrftoken']
        }

        response = self._request('DELETE', location, status_code=204, headers=header, json=False).status_code
        return response
