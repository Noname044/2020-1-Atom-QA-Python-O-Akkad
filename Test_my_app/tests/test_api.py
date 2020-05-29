import pytest


class Test_App:

    @pytest.fixture(scope='session', autouse=True)
    def setup(self, add_static_user):
        return

    @pytest.fixture(scope='function')
    def logging(self, api_client, gen_data):
        username = gen_data.get('username')
        password = gen_data.get('password')
        api_client.login(username, password)
        return api_client

    @pytest.mark.API
    def test_login(self, api_client, orm_client, gen_user):
        username = gen_user.get('username')
        password = gen_user.get('password')
        email = gen_user.get('email')
        api_client.registration(username, password, email)
        assert api_client.login(username, password).status_code == 200

        data = orm_client.select_by_username(username)
        assert data.active == 1

        api_client.logout()
        data = orm_client.select_by_username(username)
        assert data.active == 0

        api_client.login(username, password)
        api_client.del_user(username)

    @pytest.mark.API
    def test_login_badlogin_fail(self, api_client):
        username = 'Keka23'
        password = '123'
        email = '123@mail.ru'
        api_client.registration(username, password, email)
        api_client.logout()
        result = api_client.login('Keka', password).status_code
        api_client.login(username, password)
        api_client.del_user(username)
        assert result == 401

    @pytest.mark.API
    def test_login_usernotexist(self, api_client):
        username = '123123123123231'
        password = '123'
        assert api_client.login(username, password).status_code == 401

    @pytest.mark.API
    def test_add_user_fail(self, logging, orm_client, gen_user):
        username = gen_user.get('username')
        password = gen_user.get('password')
        email = gen_user.get('email')
        assert logging.add_user(username, password, email).status_code == 210
        data = orm_client.select_by_username(username)
        logging.del_user(username)
        assert data.password == password and data.email == email and data.active == 1

    @pytest.mark.API
    def test_add_bad_user_fail(self, logging, orm_client, gen_user):
        username = '123'
        password = '123'
        email = '123@123.r'
        result = logging.add_user(username, password, email).status_code

        data = orm_client.select_by_username(username)
        logging.del_user(username)
        assert data is None and result == 400

    @pytest.mark.API
    def test_add_bad_email_fail(self, logging, orm_client, gen_user):
        username = gen_user.get('username')
        password = gen_user.get('password')
        email = '123@123.r'
        result = logging.add_user(username, password, email).status_code

        data = orm_client.select_by_username(username)

        logging.del_user(username)

        assert data is None and result == 400

    @pytest.mark.API
    def test_add_emptygapes_fail(self, logging, orm_client):
        username = 'a'
        password = ''
        email = ''
        result = logging.add_user(username, password, email).status_code
        data = orm_client.select_by_username(username)

        logging.del_user(username)

        assert data is None and result == 400

    @pytest.mark.API
    def test_reg_user_fail(self, api_client, orm_client, gen_user):
        username = gen_user.get('username')
        password = gen_user.get('password')
        email = gen_user.get('email')
        result = api_client.registration(username, password, email).status_code
        data = orm_client.select_by_username(username)
        api_client.del_user(username)
        assert data.password == password and data.email == email and data.active == 1 and result == 200

    @pytest.mark.API
    def test_reg_again_user_fail(self, api_client, orm_client, gen_user):
        username = gen_user.get('username')
        password = gen_user.get('password')
        email = gen_user.get('email')
        api_client.registration(username, password, email)

        result = api_client.registration(username, password, email).status_code

        api_client.del_user(username)
        assert result == 400

    @pytest.mark.API
    def test_del_user(self, api_client, orm_client, gen_user):
        username = gen_user.get('username')
        password = gen_user.get('password')
        email = gen_user.get('email')
        api_client.registration(username, password, email)
        result = api_client.del_user(username).status_code
        data = orm_client.select_by_username(username)
        assert data is None and result == 204

    @pytest.mark.API
    def test_del_usernotexist(self, logging):
        assert logging.del_user('741147').status_code == 404

    @pytest.mark.API
    def test_block_user(self, api_client, orm_client, gen_data, gen_user):
        username = gen_user.get('username')
        password = gen_user.get('password')
        email = gen_user.get('email')
        api_client.registration(username, password, email)

        data = orm_client.select_by_username(username)
        assert data.access == 1

        assert api_client.block_user(username).status_code == 200

        data = orm_client.select_by_username(username)
        assert data.access == 0

        api_client.login(gen_data.get('username'), gen_data.get('password'))
        api_client.del_user(username)

    @pytest.mark.API
    def test_block_again_user(self, api_client, orm_client, gen_data, gen_user):
        username = gen_user.get('username')
        password = gen_user.get('password')
        email = gen_user.get('email')
        api_client.registration(username, password, email)
        api_client.block_user(username)

        data = orm_client.select_by_username(username)
        assert data.access == 0

        api_client.login(gen_data.get('username'), gen_data.get('password'))
        assert api_client.block_user(username).status_code == 304

        data = orm_client.select_by_username(username)
        assert data.access == 0

        api_client.del_user(username)

    @pytest.mark.API
    def test_accept_user(self, api_client, orm_client, gen_data, gen_user):
        username = gen_user.get('username')
        password = gen_user.get('password')
        email = gen_user.get('email')
        api_client.registration(username, password, email)

        api_client.block_user(username)
        data = orm_client.select_by_username(username)
        assert data.access == 0

        api_client.login(gen_data.get('username'), gen_data.get('password'))
        assert api_client.accept_user(username).status_code == 200
        data = orm_client.select_by_username(username)
        assert data.access == 1

        api_client.del_user(username)

    @pytest.mark.API
    def test_accept_again_user(self, api_client, orm_client, gen_data, gen_user):
        username = gen_user.get('username')
        password = gen_user.get('password')
        email = gen_user.get('email')
        api_client.registration(username, password, email)

        api_client.block_user(username)
        data = orm_client.select_by_username(username)
        assert data.access == 0

        api_client.login(gen_data.get('username'), gen_data.get('password'))
        assert api_client.accept_user(username).status_code == 200
        data = orm_client.select_by_username(username)
        assert data.access == 1

        assert api_client.accept_user(username).status_code == 304
        data = orm_client.select_by_username(username)
        assert data.access == 1

        api_client.del_user(username)

    @pytest.mark.API
    def test_status(self, api_client):
        result = api_client.status().json()
        assert result['status'] == 'ok'

    @pytest.mark.API
    def test_findmeerror_fail(self, api_client):
        assert api_client.find_me_error().status_code == 200
