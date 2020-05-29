import requests


class ResponseStatusCodeException(Exception):
    pass


class RequestErrorException(Exception):
    pass


class AppClient:

    def __init__(self, host_app, port_app):
        self.host_app = host_app
        self.port_app = port_app
        self.base_url = f'http://{self.host_app}:{self.port_app}/' # 'http://our_app:2222/'

        self.session = requests.Session()

    def login(self, user, password):
        location = f'{self.base_url}login'
        data = {
            'username': user,
            'password': password,
            'submit': 'Login'
        }
        return self.session.request('POST', location, data=data)

    def logout(self):
        location = f'{self.base_url}logout'
        return self.session.request('GET', location)

    def add_user(self, username, password, email):
        location = f'{self.base_url}api/add_user'
        data = {
            "username": username,
            "password": password,
            "email": email,
        }
        return self.session.request('POST', location, json=data)

    def registration(self, username, password, email):
        location = f'{self.base_url}reg'
        data = {
            "username": username,
            "email": email,
            "password": password,
            "confirm": password,
            "term": "y",
            "submit": "Register"
        }
        return self.session.request('POST', location, data=data)

    def del_user(self, username):
        location = f'{self.base_url}api/del_user/{username}'
        return self.session.request('GET', location)

    def block_user(self, username):
        location = f'{self.base_url}api/block_user/{username}'
        return self.session.request('GET', location)

    def accept_user(self, username):
        location = f'{self.base_url}api/accept_user/{username}'
        return self.session.request('GET', location)

    def status(self):
        location = f'{self.base_url}status'
        return self.session.request('GET', location)

    def find_me_error(self):
        location = f'{self.base_url}static/scripts/findMeError.js'
        return self.session.request('GET', location)
