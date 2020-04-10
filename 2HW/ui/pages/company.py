import time

from ui.locators.locators import EnterLocators, CompanyLocators
from ui.pages.base import BasePage


class CompanyPage(BasePage):
    locators = CompanyLocators()

    def creating(self, name, address, picture):
        self.click(self.locators.COMPANY_BUTTON)
        time.sleep(5)
        self.click(self.locators.CREATE_COMPANY_BUTTON)
        self.click(self.locators.TARGET)
        self.inputting(address, self.locators.ADDRESS_FORM)
        time.sleep(5)
        self.inputting(name, self.locators.COMP_NAME)
        self.click(self.locators.FORM_ADV)
        self.input_object(picture, self.locators.PICTURE)
        self.click(self.locators.SAVE)
        self.click(self.locators.ADD_ADV)
        return self.click(self.locators.SUBMIT)
