from ui.locators.locators import MainLocators
from ui.pages.base import BasePage


class MainPage(BasePage):
    locators = MainLocators()

    def logout(self):
        return self.click(self.locators.LOGOUT)

    def check_data(self):
        return self.find(self.locators.DATA).text
