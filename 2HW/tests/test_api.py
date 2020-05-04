import pytest

from apihw.api.client import TargetClient


class Test_Target:

    @pytest.fixture(scope='function')
    def api_client(self):
        email = 'Cheburekoff3@ya.ru',
        password = '89775114232Pol',
        return TargetClient(email, password)

    @pytest.mark.API
    def test_create(self, api_client):
        assert api_client.post_audit('Mylist456')['name'] == 'Mylist456'

    @pytest.mark.API
    def test_delete(self, api_client):
        id = api_client.post_audit('Mylist456545')['id']
        assert api_client.delete_audit(id) == 204
