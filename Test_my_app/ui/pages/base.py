from selenium.common.exceptions import StaleElementReferenceException

from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from ui.locators.locators import BaseLocators

RETRY_COUNT = 3


class BasePage:
    locators = BaseLocators()

    def __init__(self, driver):
        self.driver = driver

    def find(self, locator, timeout=None) -> WebElement:
        return self.wait(timeout).until(EC.presence_of_element_located(locator))

    def alert(self, msg):
        script = "alert('{}')".format(msg)
        self.driver.execute_script(script)

    def click(self, locator, timeout=None):
        for i in range(RETRY_COUNT):
            try:
                self.find(locator)
                element = self.wait(timeout).until(EC.element_to_be_clickable(locator))
                element.click()
                return

            except StaleElementReferenceException:
                if i < RETRY_COUNT - 1:
                    pass
        raise

    def scroll_to_element(self, element):
        self.driver.execute_script('arguments[0].scrollIntoView(true);', element)

    def wait(self, timeout=None):
        if timeout is None:
            timeout = 5
        return WebDriverWait(self.driver, timeout=timeout)

    def count_elements(self, locator, count, timeout=1):
        self.wait(timeout).until(lambda browser: len(browser.find_elements(*locator)) == count)

    def inputting(self, smth, locator):
        input_element = self.find(locator)
        input_element.clear()
        input_element.send_keys(smth)
