import time

from ui.locators.locators import EnterLocators
from ui.pages.base import BasePage


class EnterPage(BasePage):
    locators = EnterLocators()

    def authorization(self, login, password):
        self.click(self.locators.ENTER_BUTTON)
        self.inputting(login, self.locators.EMAIL_FORM)
        self.inputting(password, self.locators.PASSWORD_FORM)
        return self.click(self.locators.CLICK_BUTTON)
