from db_clients.models import UsersTests
from db_clients.orm_client import OrmConnector


class OrmBuilder:

    def __init__(self, connection: OrmConnector):
        self.connection = connection
        self.engine = connection.connection.engine
        self.table = UsersTests

    def select_by_username(self, username) -> UsersTests:
        self.connection.session.expire_all()
        result = self.connection.session.query(self.table).filter(self.table.username == username).first()
        return result
