import pytest
import os

from ui.pages.audit import AuditPage
from ui.pages.base import BasePage
from ui.pages.company import CompanyPage
from ui.pages.enter import EnterPage


class BaseCase:

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, config, request):
        self.driver = driver
        self.config = config
        self.base_page: BasePage = request.getfixturevalue('base_page')
        self.enter_page: EnterPage = request.getfixturevalue('enter_page')
        self.company_page: CompanyPage = request.getfixturevalue('company_page')
        self.audit_page: AuditPage = request.getfixturevalue('audit_page')

    @pytest.fixture(scope='function')
    def auth(self):
        return self.enter_page.authorization("Cheburekoff3@ya.ru", "89775114232Pol")
