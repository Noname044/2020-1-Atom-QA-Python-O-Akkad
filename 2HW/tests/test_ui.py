import time

import pytest
from selenium.common.exceptions import TimeoutException, ElementNotInteractableException

from tests.base import BaseCase


class Test(BaseCase):
    @pytest.mark.UI
    def test_entering(self):
        self.enter_page.authorization("Cheburekoff3@ya.ru", "89775114232Pol")
        assert "Error" not in self.driver.page_source

    @pytest.mark.UI
    def test_fail_entering(self):
        self.enter_page.authorization("78Cheburekoff3@ya.ru", "7889775114232Pol")
        assert "Error" in self.driver.page_source

    @pytest.mark.UI
    def test_create_company(self, auth):
        self.company_page.creating("Mycompany123", "https://www.google.com/", "jr.jpeg")
        time.sleep(3)
        assert "Mycompany123" in self.driver.page_source

    @pytest.mark.UI
    def test_create_audit(self, auth):
        self.audit_page.create_audit("Myaudit123")
        self.audit_page.search_audit("Myaudit123")
        time.sleep(5)
        assert "Myaudit123" in self.driver.page_source

    @pytest.mark.UI
    def test_delete_audit(self, auth):
        self.audit_page.create_audit("Myaudit1234")
        self.audit_page.delete_audit("Myaudit1234")
        self.audit_page.search_audit("Myaudit1234")
        time.sleep(5)
        assert "Myaudit1234" not in self.driver.page_source
