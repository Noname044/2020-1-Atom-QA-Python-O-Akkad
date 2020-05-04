import pytest

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

    @pytest.mark.UI_t
    def test_create_company(self, auth):
        self.company_page.creating("Mycompany123", "https://www.google.com/", "jr.jpeg")
        self.company_page.searching("Mycompany123")
        assert self.audit_page.find(self.company_page.locators.MY_COMP).text == "Mycompany123"

    @pytest.mark.UI
    def test_create_audit(self, auth):
        self.audit_page.create_audit("Myaudit123")
        self.audit_page.search_audit("Myaudit123")
        assert self.audit_page.find(self.audit_page.locators.MY_AUDIT).text == "Myaudit123"

    @pytest.mark.UI
    def test_delete_audit(self, auth):
        self.audit_page.create_audit("Myaudit1234")
        self.audit_page.delete_audit("Myaudit1234")
        assert self.audit_page.find(self.audit_page.locators.MY_AUDIT).text != "Myaudit1234"
