from mysql_3.mysql_client.mysql_client import MysqlConnector
from mysql_3.check_log.check_log_sql import CheckingLogs


class MysqlBuilder:

    def __init__(self, connection: MysqlConnector):
        self.connection = connection
        self.create_tables()
        self.check = CheckingLogs(self.connection)

    def create_tables(self):
        total_number = """
            create table total_number (
                total char(5) not null
            )
            """
        self.connection.execute_query(total_number)
        num_of_req = """
            create table number_of_requests(
                Type char(5) not null,
                Number char(5) not null
            )
            """
        self.connection.execute_query(num_of_req)
        top1 = """
            create table top10_by_size(
                Number char(2) not null,
                URL char(20) not null,
                Code char(3) not null,
                Size char(10) not null,
                Count char(5) not null
            )
            """
        self.connection.execute_query(top1)
        top2 = """
            create table top10_by_client_error(
                Number char(2) not null,
                URL char(20) not null,
                Code char(3) not null,
                IP char(15) not null,
                Count char(5) not null
            )
            """
        self.connection.execute_query(top2)
        top3 = """
                create table top10_by_redirect(
                    Number char(2) not null,
                    URL char(20) not null,
                    Code char(3) not null,
                    IP char(15) not null,
                    Count char(5) not null
                )
                """
        self.connection.execute_query(top3)

    def add_statistic(self, inp):
        self.check.main(inp)

