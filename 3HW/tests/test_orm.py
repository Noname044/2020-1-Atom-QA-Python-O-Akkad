import pytest

from mysql_3.orm_client.orm_client import OrmConnector
from mysql_3.builder.orm_builder import OrmBuilder


class Test:

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, orm_client):
        self.orm: OrmConnector = orm_client
        self.builder = OrmBuilder(orm_client)

    def test(self):
        inp = '../access.log'

        self.builder.add_statistic(inp)
