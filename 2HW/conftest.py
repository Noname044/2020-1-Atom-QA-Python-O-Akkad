from ui.fixtures import *
import pytest


class UsupportedBrowserException(Exception):
    pass


def pytest_addoption(parser):
    parser.addoption('--url', default='https://target.my.com/')
    parser.addoption('--browser', default='chrome')
    parser.addoption('--browser_ver', default='latest')
    parser.addoption('--selenoid', default=None)
    parser.addoption('--ver_for_selenoid', default='80.0')


@pytest.fixture(scope='session')
def config(request):
    url = request.config.getoption('--url')
    browser = request.config.getoption('--browser')
    version = request.config.getoption('--browser_ver')
    selenoid = request.config.getoption('--selenoid')
    ver_for_selenoid = request.config.getoption('--ver_for_selenoid')

    return {'browser': browser, 'version': version, 'url': url, 'selenoid': selenoid,
            'ver_for_selenoid': ver_for_selenoid}
