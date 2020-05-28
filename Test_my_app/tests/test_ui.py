import pytest
import requests

from selenium.webdriver import ActionChains

from tests.base import BaseCase


@pytest.mark.usefixtures("take_screenshot_when_failure")
class Test(BaseCase):

    @pytest.mark.UI
    def test_entering(self, auth):
        assert "Welcome!" in self.driver.page_source

    @pytest.mark.UI
    def test_fail_entering(self, gen_user):
        username = gen_user.get('username')
        password = gen_user.get('password')
        self.enter_page.authorization(username, password)
        assert 'Invalid username or password' in self.driver.page_source

    @pytest.mark.UI
    def test_registration(self, gen_user):
        username = gen_user.get('username')
        password = gen_user.get('password')
        email = gen_user.get('email')
        self.enter_page.registration(username, email, password)
        result = self.mysql.execute_query(f"select username, email, password "
                                          f"from test_users "
                                          f"where username = '{username}'")
        assert result[0] == (username, email, password)
        assert "Welcome!" in self.driver.page_source
        self.mysql.execute_query(f"delete from test_users where username = '{username}';")

    @pytest.mark.UI
    def test_fail_registration_existuser(self, gen_user):
        username = self.gen.get('username')
        password = gen_user.get('password')
        email = gen_user.get('email')
        self.enter_page.registration(username, email, password)
        result = self.mysql.execute_query(f"select username, email, password "
                                          f"from test_users "
                                          f"where username = '{username}'")
        assert result[0] != (username, email, password)
        assert "Welcome!" not in self.driver.page_source

    @pytest.mark.UI
    def test_fail_registration_existemail(self, gen_user):
        email = self.gen.get('email')
        username = gen_user.get('username')
        password = gen_user.get('password')
        self.enter_page.registration(username, email, password)
        result = self.mysql.execute_query(f"select username, email, password "
                                          f"from test_users "
                                          f"where username = '{username}'")
        assert result == ()
        assert 'This email is used by other user' in self.driver.page_source

    @pytest.mark.UI
    def test_fail_registration_incorrect_data(self):
        username = "Kex"
        email = "kex@mailu"
        password = "jhhg2"
        self.enter_page.registration(username, email, password)
        result = self.mysql.execute_query(f"select username, email, password "
                                          f"from test_users "
                                          f"where username = '{username}'")
        assert result == ()
        assert f"{username}: Incorrect username length, {email}: Invalid email address" in self.driver.page_source

    @pytest.mark.UI
    def test_logout(self, auth):
        self.main_page.logout()
        assert 'Welcome to the TEST SERVER' in self.driver.page_source

    @pytest.mark.UI
    def test_data_vk_id(self, auth):
        username = self.gen.get('username')

        url = f'http://{self.config["host_vk"]}:{self.config["port_vk"]}/vk_id/{username}'

        result = requests.get(url).json()
        vk_id = result['vk_id']

        assert self.main_page.check_data() == f'Logged as {username}\nVK ID: {vk_id}'

    @pytest.mark.UI
    def test_data_empty_vk_id(self, gen_user):
        username = gen_user.get('username')
        password = gen_user.get('password')
        email = gen_user.get('email')
        self.enter_page.registration(username, email, password)

        url = f'http://{self.config["host_vk"]}:{self.config["port_vk"]}/vk_id/{username}'
        result = requests.get(url)
        assert result.status_code == 404 and result.json() == {}

        assert self.main_page.check_data() == f'Logged as {username}'

        self.main_page.logout()

        url = f'http://{self.config["host_vk"]}:{self.config["port_vk"]}/{username}/adduser'
        result = requests.get(url).json()
        vk_id = result['vk_id']

        self.enter_page.authorization(username, password)
        assert self.main_page.check_data() == f'Logged as {username}\nVK ID: {vk_id}'
        url = f'http://{self.config["host_vk"]}:{self.config["port_vk"]}/{username}/deluser'
        requests.get(url)
        self.mysql.execute_query(f"delete from test_users where username = '{username}';")

    @pytest.mark.UI
    def test_click_api(self, auth):
        window_before = self.driver.window_handles[0]

        self.main_page.click(self.main_page.locators.API)
        window_after = self.driver.window_handles[1]
        self.driver.switch_to.window(window_after)

        assert "Application programming interface" in self.driver.page_source

        self.driver.close()
        self.driver.switch_to.window(window_before)

    @pytest.mark.UI
    def test_click_internet(self, auth):
        window_before = self.driver.window_handles[0]

        self.main_page.click(self.main_page.locators.INTERNET)
        window_after = self.driver.window_handles[1]
        self.driver.switch_to.window(window_after)

        assert "What Will the Internet Be Like in the Next 50 Years?" in self.driver.page_source

        self.driver.close()
        self.driver.switch_to.window(window_before)

    @pytest.mark.UI
    def test_click_smtp(self, auth):
        window_before = self.driver.window_handles[0]

        self.main_page.click(self.main_page.locators.SMTP)
        window_after = self.driver.window_handles[1]
        self.driver.switch_to.window(window_after)

        assert "SMTP" in self.driver.page_source

        self.driver.close()
        self.driver.switch_to.window(window_before)

    @pytest.mark.UI
    def test_tm(self, auth):
        self.main_page.click(self.main_page.locators.TM)
        assert "Welcome!" in self.driver.page_source

    @pytest.mark.UI
    def test_home(self, auth):
        self.main_page.click(self.main_page.locators.HOME)
        assert "Welcome!" in self.driver.page_source

    @pytest.mark.UI
    def test_python(self, auth):
        self.main_page.click(self.main_page.locators.PYTHON)
        assert "Python" in self.driver.page_source

    @pytest.mark.UI
    def test_phistory(self, auth):
        action = ActionChains(self.main_page.driver)
        elem = self.main_page.find(self.main_page.locators.PYTHON)
        action.move_to_element(elem).perform()
        self.main_page.click(self.main_page.locators.PHISTORY)
        assert "History of Python" in self.driver.page_source

    @pytest.mark.UI
    def test_pflask(self, auth):
        window_before = self.driver.window_handles[0]
        action = ActionChains(self.main_page.driver)
        elem = self.main_page.find(self.main_page.locators.PYTHON)
        action.move_to_element(elem).perform()
        self.main_page.click(self.main_page.locators.PFLASK)
        window_after = self.driver.window_handles[1]
        self.driver.switch_to.window(window_after)
        assert "Welcome to Flask’s documentation." in self.driver.page_source
        self.driver.close()
        self.driver.switch_to.window(window_before)

    # !!!!!!!!!!!!!!
    @pytest.mark.UI
    def test_fail_linux(self, auth):
        window_before = self.driver.window_handles[0]
        action = ActionChains(self.main_page.driver)
        elem = self.main_page.find(self.main_page.locators.LINUX)
        action.move_to_element(elem).perform()
        self.main_page.click(self.main_page.locators.CENTOS)
        window_after = self.driver.window_handles[1]
        self.driver.switch_to.window(window_before)
        self.driver.close()
        self.driver.switch_to.window(window_after)
        assert "CentOS" in self.driver.page_source

    @pytest.mark.UI
    def test_wnews(self, auth):
        window_before = self.driver.window_handles[0]
        action = ActionChains(self.main_page.driver)
        elem = self.main_page.find(self.main_page.locators.NETWORK)
        action.move_to_element(elem).perform()
        self.main_page.click(self.main_page.locators.WNEWS)
        window_after = self.driver.window_handles[1]
        self.driver.switch_to.window(window_after)
        assert "Wireshark" in self.driver.page_source
        self.driver.close()
        self.driver.switch_to.window(window_before)

    @pytest.mark.UI
    def test_wdownload(self, auth):
        window_before = self.driver.window_handles[0]
        action = ActionChains(self.main_page.driver)
        elem = self.main_page.find(self.main_page.locators.NETWORK)
        action.move_to_element(elem).perform()
        self.main_page.click(self.main_page.locators.WDOWNLOAD)
        window_after = self.driver.window_handles[1]
        self.driver.switch_to.window(window_after)
        assert "Download Wireshark" in self.driver.page_source
        self.driver.close()
        self.driver.switch_to.window(window_before)

    @pytest.mark.UI
    def test_wexample(self, auth):
        window_before = self.driver.window_handles[0]
        action = ActionChains(self.main_page.driver)
        elem = self.main_page.find(self.main_page.locators.NETWORK)
        action.move_to_element(elem).perform()
        self.main_page.click(self.main_page.locators.WEXAMPLE)

        window_after = self.driver.window_handles[1]
        self.driver.switch_to.window(window_after)

        assert "Tcpdump Examples" in self.driver.page_source
        self.driver.close()
        self.driver.switch_to.window(window_before)
