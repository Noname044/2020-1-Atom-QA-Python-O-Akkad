import pytest
import allure
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from ui.pages.base import BasePage
from ui.pages.enter import EnterPage
from ui.pages.main import MainPage
from webdriver_manager.chrome import ChromeDriverManager


class UsupportedBrowserException(Exception):
    pass


@pytest.fixture(scope='function')
def base_page(driver):
    return BasePage(driver)


@pytest.fixture(scope='function')
def enter_page(driver):
    return EnterPage(driver)


@pytest.fixture(scope='function')
def main_page(driver):
    return MainPage(driver)


@pytest.fixture(scope='function')
def driver(config):
    browser = config['browser']
    version = config['version']
    url = config['url']
    selenoid = config['selenoid']
    ver_for_selenoid = config['ver_for_selenoid']

    if browser == 'chrome':
        options = ChromeOptions()
        options.add_argument("--window-size=800,600")

        if selenoid:

            capabilities = {'acceptInsecureCerts': True,
                            'browserName': 'chrome',
                            'version': ver_for_selenoid,
                            }

            driver = webdriver.Remote(command_executor=f'http://{selenoid}/wd/hub/',
                                      options=options,
                                      desired_capabilities=capabilities
                                      )
        else:
            manager = ChromeDriverManager(version=version)
            driver = webdriver.Chrome(executable_path=manager.install(),
                                      options=options,
                                      desired_capabilities={'acceptInsecureCerts': True}
                                      )

    else:
        raise UsupportedBrowserException(f'Usupported browser: "{browser}"')

    driver.get(url)
    driver.maximize_window()
    yield driver
    driver.close()


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep" + rep.when, rep)
    return rep


@pytest.fixture(scope="function")
def take_screenshot_when_failure(request, driver):
    yield
    if request.node.repcall.failed:
        messages = [k['message'] for k in driver.get_log('browser')]
        allure.attach('\n'.join(messages),
                      name='console.log',
                      attachment_type=allure.attachment_type.TEXT)
        allure.attach(driver.get_screenshot_as_png(),
                      name=request.node.location[-1],
                      attachment_type=allure.attachment_type.PNG)
