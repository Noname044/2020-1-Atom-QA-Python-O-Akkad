from mysql_3.models.models import Base
from mysql_3.check_log.check_log_orm import CheckingLogs
from mysql_3.orm_client.orm_client import OrmConnector


class OrmBuilder:

    def __init__(self, connection: OrmConnector):
        self.connection = connection
        self.engine = connection.connection.engine
        self.create_tables()
        self.check = CheckingLogs(self.connection)

    def create_tables(self):
        if not self.engine.dialect.has_table(self.engine, 'total_number'):
            Base.metadata.tables['total_number'].create(self.engine)

        if not self.engine.dialect.has_table(self.engine, 'number_of_requests'):
            Base.metadata.tables['number_of_requests'].create(self.engine)

        if not self.engine.dialect.has_table(self.engine, 'top10_by_size'):
            Base.metadata.tables['top10_by_size'].create(self.engine)

        if not self.engine.dialect.has_table(self.engine, 'top10_by_client_error'):
            Base.metadata.tables['top10_by_client_error'].create(self.engine)

        if not self.engine.dialect.has_table(self.engine, 'top10_by_redirect'):
            Base.metadata.tables['top10_by_redirect'].create(self.engine)

    def add_statistic(self, inp):
        self.check.main(inp)










