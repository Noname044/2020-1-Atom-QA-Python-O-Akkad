import time

from attr import exceptions, exceptions

from ui.locators.locators import EnterLocators, AuditLocators
from ui.pages.base import BasePage


class AuditPage(BasePage):
    locators = AuditLocators()

    def create_audit(self, name):
        self.click(self.locators.AUDIT_BUTTON)
        try:
            self.click(self.locators.CREATE_AUDIT)
        except:
            self.click(self.locators.CREATE_OM_AUDIT)
        time.sleep(10)
        self.click(self.locators.CREATE_AUDIT_BUTTON)
        self.click(self.locators.ADD_MY_LIST)
        self.click(self.locators.SUBMIT_LIST)
        self.inputting(name, self.locators.AUDIT_NAME)
        return self.click(self.locators.SUBMIT_CREATION)

    def delete_audit(self, name):
        self.wait()
        self.click(self.locators.AUDIT_BUTTON)
        self.wait()
        self.search_audit(name)
        self.click(self.locators.SUG)
        time.sleep(5)
        self.click(self.locators.DELETE_AUDIT)
        time.sleep(5)
        return self.click(self.locators.CONFIRM_DELETING)

    def search_audit(self, name):
        self.search(name, self.locators.SEARCH_AUDIT)
