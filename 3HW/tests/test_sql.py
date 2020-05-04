import pytest

from mysql_3.mysql_client.mysql_client import MysqlConnector
from mysql_3.builder.mysql_builder import MysqlBuilder


class Test:

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, mysql_client):
        self.mysql: MysqlConnector = mysql_client
        self.builder = MysqlBuilder(mysql_client)

    def test(self):
        inp = '../access.log'

        self.builder.add_statistic(inp)

        total = self.mysql.execute_query('select * from total_number')
        req = self.mysql.execute_query('select * from number_of_requests')
        top1 = self.mysql.execute_query('select * from top10_by_size')
        top2 = self.mysql.execute_query('select * from top10_by_client_error')
        top3 = self.mysql.execute_query('select * from top10_by_redirect')

        print(total)
        print(req)
        print(top1)
        print(top2)
        print(top3)
