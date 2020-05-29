import pymysql


class MysqlConnector:

    def __init__(self, user, password, db_name, host_db, port_db):
        self.user = user
        self.password = password
        self.db_name = db_name
        self.host = host_db#'app_db'
        self.port = port_db#3306
        self.connection = self.get_connection(db_created=True)

    def get_connection(self, db_created=False):
        return pymysql.connect(
            host=self.host,
            port=self.port,
            user=self.user,
            password=self.password,
            db=self.db_name if db_created else None,
            charset='utf8',
            autocommit=True,

        )

    def execute_query(self, query):
        cursor = self.connection.cursor()
        cursor.execute(query)
        res = cursor.fetchall()

        return res
