import pytest
import requests

from mock_4.mock import mock
from mock_4.socket_client.socet_client import SocketClient
from mysql_3.mysql_client.mysql_client import MysqlConnector
from mysql_3.orm_client.orm_client import OrmConnector
from ssh_5.connection.connection import SSH


@pytest.fixture(scope='session')
def mysql_client():
    return MysqlConnector('user', 'password', 'DB_Logger')


@pytest.fixture(scope='session')
def orm_client():
    return OrmConnector('user', 'password', 'DB_ORM_Logger')


@pytest.fixture(scope='session')
def mock_server():
    server = mock.run_mock()
    server_host = server._kwargs['host']
    server_port = server._kwargs['port']

    yield server_host, server_port

    shutdown_url = f'http://{server_host}:{server_port}/shutdown'
    requests.get(shutdown_url)


@pytest.fixture(scope='session')
def socket_client():
    return SocketClient('127.0.0.1', 5000)

@pytest.fixture(scope='session')
def ssh_client():
    return SSH
