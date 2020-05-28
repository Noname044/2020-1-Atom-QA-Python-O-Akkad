from selenium.webdriver.common.by import By


class BaseLocators:
    LOGOUT = (By.CLASS_NAME, 'uk-button.uk-button-danger')


class EnterLocators:
    NAME_FORM = (By.ID, 'username')
    PASSWORD_FORM = (By.ID, 'password')
    ENTER_BUTTON = (By.CLASS_NAME, "uk-button.uk-button-primary.uk-button-large.uk-width-1-1")
    CREATE_AC = (By.XPATH, '//a[@href="/reg"]')
    EMAIL_FORM = (By.ID, 'email')
    CONFIRM_FORM = (By.ID, 'confirm')
    ACCEPT_BOX = (By.ID, 'term')
    ERROR = (By.CLASS_NAME, 'uk-alert.uk-alert-warning.uk-margin-small-top.uk-text-center')
    DANGER = (By.CLASS_NAME, 'uk-alert.uk-alert-danger.uk-margin-small-top.uk-text-center')
    MESSAGE = (By.CLASS_NAME, 'uk-alert.uk-alert-message.uk-margin-small-top.uk-text-center')

class MainLocators:
    LOGOUT = (By.CLASS_NAME, 'uk-button.uk-button-danger')
    WLLCM = (By.CLASS_NAME, 'uk-card-title.uk-text-center')
    DATA = (By.CLASS_NAME, 'uk-text-bold')
    API = (By.XPATH, '//a[@href="https://en.wikipedia.org/wiki/Application_programming_interface"]')
    INTERNET = (By.XPATH, '//a[@href="https://www.popularmechanics.com/technology/infrastructure/a29666802/future-of-the-internet/"]')
    SMTP = (By.XPATH, '//a[@href="https://ru.wikipedia.org/wiki/SMTP"]')

    TM = (By.CLASS_NAME, 'uk-navbar-brand.uk-hidden-small')
    HOME = (By.XPATH, '//a[@href="/"]')

    PYTHON = (By.XPATH, '//a[@href="https://www.python.org/"]')
    PHISTORY = (By.XPATH, '//a[@href="https://en.wikipedia.org/wiki/History_of_Python"]')
    PFLASK = (By.XPATH, '//a[@href="https://flask.palletsprojects.com/en/1.1.x/#"]')

    LINUX  = (By.XPATH, '//li[3]')
    CENTOS = (By.XPATH, '//a[@href="https://getfedora.org/ru/workstation/download/"]')

    NETWORK = (By.XPATH, '//li[4]')
    WNEWS = (By.XPATH, '//a[@href="https://www.wireshark.org/news/"]')
    WDOWNLOAD = (By.XPATH, '//a[@href="https://www.wireshark.org/#download"]')
    WEXAMPLE = (By.XPATH, '//a[@href="https://hackertarget.com/tcpdump-examples/"]')
