import psycopg2
from sqlalchemy import create_engine, text, select, column, table

class DBConn:
    __instance = None
    def __new__(cls, *args, **kwargs):
        if not isinstance(cls.__instance, cls):
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self, user, passwd):
        self.host = "localhost"
        self.port = "5432"
        self.user = user
        self.passwd = passwd
        self.db = "flown_data"
        self.conn  = self.connect()
        self.message = "Подключение выполнено успешно"

    def connect(self):
        try:
            return create_engine(f'postgresql://{self.user}:{self.passwd}@{self.host}:{self.port}/{self.db}')

        except OperationalError as e:
            print(f"Ошибка подключения к базе данных: {e}")
        except SQLAlchemyError as e:
            print(f"Общая ошибка SQLAlchemy: {e}")

    def close(self):
        if self.conn:
            self.conn.close()
            print("Connection closed!")

    def get_format(self):
        format_table = table('formats', column('id'), column('extens'))
        with self.conn.connect() as conn:
            data = select(format_table)
            result = conn.execute(data).mappings().all()
            output_dict = {}
            for item in result:
                output_dict[item['extens']] = item['id']
                output_dict["tiff"] = 2
        return output_dict

    def get_secret(self):
        secret_table = table('secret', column('id'), column('cl'))
        with self.conn.connect() as conn:
            data = select(secret_table)
            result = conn.execute(data).mappings().all()
            output_dict = {}
            for item in result:
                output_dict[item['cl']] = item['id']
        return output_dict

    def get_contract(self):
        contract_table = table('contracts', column('id'), column('cipher'))
        with self.conn.connect() as conn:
            data = select(contract_table)
            result = conn.execute(data).mappings().all()
            output_dict = {}
            for item in result:
                output_dict[item['cipher']] = item['id']
        return output_dict

    def get_companies(self):
        companies_table = table('companies', column('id'), column('name'))
        with self.conn.connect() as conn:
            data = select(companies_table)
            result = conn.execute(data).mappings().all()
            output_dict = {}
            for item in result:
                output_dict[item['name']] = item['id']
        return output_dict

