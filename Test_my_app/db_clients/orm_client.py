import sqlalchemy
from sqlalchemy.orm import sessionmaker


class OrmConnector:

    def __init__(self, user, password, db_name, host_db, port_db):
        self.user = user
        self.password = password
        self.db_name = db_name
        self.host = host_db#'app_db'
        self.port = port_db#3306
        self.connection = self.get_connection(db_created=True)
        session = sessionmaker(bind=self.connection.engine, autocommit=True, enable_baked_queries=False)
        self.session = session()

    def get_connection(self, db_created=False):
        engine = sqlalchemy.create_engine(
            'mysql+pymysql://{user}:{password}@{host}:{port}/{db}'.format(user=self.user,
                                                                          password=self.password,
                                                                          host=self.host,
                                                                          port=self.port,
                                                                          db=self.db_name if db_created else ''),
            encoding='utf8'
        )
        return engine.connect()

    def execute_query(self, query):
        res = self.connection.execute(query)
        return res.getchall()


