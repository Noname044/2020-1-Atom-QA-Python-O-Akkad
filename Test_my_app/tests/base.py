import pytest

from db_clients.mysql_client import MysqlConnector
from ui.pages.base import BasePage
from ui.pages.enter import EnterPage
from ui.pages.main import MainPage


class BaseCase:

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, config, request, mysql_client, add_static_user, set_vk_mock, gen_data):
        self.driver = driver
        self.config = config
        self.base_page: BasePage = request.getfixturevalue('base_page')
        self.enter_page: EnterPage = request.getfixturevalue('enter_page')
        self.main_page: MainPage = request.getfixturevalue('main_page')
        self.mysql: MysqlConnector = mysql_client
        self.gen = gen_data

    @pytest.fixture(scope='function')
    def auth(self, gen_data):
        return self.enter_page.authorization(gen_data.get('username'), gen_data.get('password'))

