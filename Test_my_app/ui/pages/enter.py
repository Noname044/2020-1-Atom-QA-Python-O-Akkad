from ui.locators.locators import EnterLocators
from ui.pages.base import BasePage


class EnterPage(BasePage):
    locators = EnterLocators()

    def authorization(self, name, password):
        self.inputting(name, self.locators.NAME_FORM)
        self.inputting(password, self.locators.PASSWORD_FORM)
        return self.click(self.locators.ENTER_BUTTON)

    def registration(self, name, email, password):
        self.click(self.locators.CREATE_AC)
        self.inputting(name, self.locators.NAME_FORM)
        self.inputting(email, self.locators.EMAIL_FORM)
        self.inputting(password, self.locators.PASSWORD_FORM)
        self.inputting(password, self.locators.CONFIRM_FORM)
        self.click(self.locators.ACCEPT_BOX)
        return self.click(self.locators.ENTER_BUTTON)
