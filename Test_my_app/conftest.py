import pytest
import random

import requests

from api.client import AppClient
from db_clients.mysql_client import MysqlConnector
from db_clients.orm_builder import OrmBuilder
from db_clients.orm_client import OrmConnector
from ui.fixtures import *


class UsupportedBrowserException(Exception):
    pass


def pytest_addoption(parser):
    parser.addoption('--url', default='http://our_app:2222/')
    parser.addoption('--browser', default='chrome')
    parser.addoption('--browser_ver', default='latest')
    parser.addoption('--selenoid', default=None)
    parser.addoption('--ver_for_selenoid', default='81.0')


@pytest.fixture(scope='session')
def config(request):
    url = request.config.getoption('--url')
    browser = request.config.getoption('--browser')
    version = request.config.getoption('--browser_ver')
    selenoid = request.config.getoption('--selenoid')
    ver_for_selenoid = request.config.getoption('--ver_for_selenoid')

    host_db = 'app_db'
    port_db = 3306

    host_app = 'our_app'
    port_app = 2222

    host_vk = 'vk_mock'
    port_vk = 5000

    return {'browser': browser,
            'version': version,
            'url': url,
            'selenoid': selenoid,
            'ver_for_selenoid': ver_for_selenoid,
            'host_db': host_db, 'port_db': port_db,
            'host_app': host_app, 'port_app': port_app,
            'host_vk': host_vk, 'port_vk': port_vk}


@pytest.fixture(scope='module')
def mysql_client(config):
    return MysqlConnector('test_qa', 'qa_test', 'apptest', config['host_db'], config['port_db'])


@pytest.fixture(scope='module')
def orm_client(config):
    connect = OrmConnector('test_qa', 'qa_test', 'apptest', config['host_db'], config['port_db'])
    return OrmBuilder(connect)


@pytest.fixture(scope='session')
def api_client(config):
    return AppClient(config['host_app'], config['port_app'])


@pytest.fixture(scope='session')
def gen_data():
    with open('../emails.txt', 'r') as file:
        lines = file.readlines()
        line = random.choice(lines).split(' ')

    return {'email': line[0],
            'username': line[0].split('@')[0],
            'password': line[1][:-1]}


@pytest.fixture(scope='function')
def gen_user():
    with open('../emails.txt', 'r') as file:
        lines = file.readlines()
        line = random.choice(lines).split(' ')

    return {'email': line[0],
            'username': line[0].split('@')[0],
            'password': line[1][:-1]}


@pytest.fixture(scope='session')
def add_static_user(config, gen_data):
    session = requests.Session()
    location = f'http://{config.get("host_app")}:{config.get("port_app")}/reg'
    data = {
        "username": gen_data.get('username'),
        "email": gen_data.get('email'),
        "password": gen_data.get('password'),
        "confirm": gen_data.get('password'),
        "term": "y",
        "submit": "Register"
    }

    yield session.request('POST', location, data=data)

    location = f'http://{config.get("host_app")}:{config.get("port_app")}/api/del_user/{gen_data.get("username")}'
    session.request('GET', location)


@pytest.fixture(scope='session')
def set_vk_mock(config, gen_data):
    username = gen_data.get("username")
    url = f'http://{config["host_vk"]}:{config["port_vk"]}/{username}/adduser'
    requests.get(url).json()

    yield

    url = f'http://{config["host_vk"]}:{config["port_vk"]}/{username}/deluser'
    requests.get(url)
