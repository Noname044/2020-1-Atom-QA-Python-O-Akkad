import pytest

from selenium import webdriver
from selenium.webdriver import ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager

from ui.pages.audit import AuditPage
from ui.pages.base import BasePage
from ui.pages.company import CompanyPage
from ui.pages.enter import EnterPage


class UsupportedBrowserException(Exception):
    pass


@pytest.fixture(scope='function')
def base_page(driver):
    return BasePage(driver)


@pytest.fixture(scope='function')
def enter_page(driver):
    return EnterPage(driver)


@pytest.fixture(scope='function')
def company_page(driver):
    return CompanyPage(driver)


@pytest.fixture(scope='function')
def audit_page(driver):
    return AuditPage(driver)


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
