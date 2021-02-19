import psycopg2

from app.db.db_teller import DataBase
from app.db.transactioncm import TransactionCtx


CONNECT_LINE = 'postgres://testapi:testAPIpasswd@localhost/testapidb'


class PostgresDB(DataBase):

    def __init__(self):
        super().__init__()
        self.db_name = 'SQL Database'

    def add_user(self, _first_name, _middle_name, _last_name):
        """Создание нового объекта user c указанными полями."""
        _SQL = f"""
                INSERT INTO users (first_name, middle_name, last_name)
                VALUES
                ('{_first_name}', '{_middle_name}', '{_last_name}')
                """
        with psycopg2.connect(CONNECT_LINE) as conn:
            with TransactionCtx(conn) as transaction:
                with conn.cursor() as cursor:
                    try:
                        cursor.execute(_SQL)
                    except:
                        print('Some error')

    def get_user(self, _user_id):
        """Возвращает объект пользователя с указанным user_id."""
        _SQL = f"""
                SELECT user_id, first_name, middle_name, last_name
                FROM users
                WHERE user_id = {_user_id}
                """
        with psycopg2.connect(CONNECT_LINE) as conn:
            with TransactionCtx(conn) as transaction:
                with conn.cursor() as cursor:
                    cursor.execute(_SQL)
                    data = cursor.fetchall()
        if data:
            return self.data_to_dict(data[0])

        return None

    def update_user(self, _user_id, _first_name, _middle_name, _last_name):
        """Обновляет указанные данные объекта user по user_id"""
        _SQL = f"""
                UPDATE users
                SET first_name = '{_first_name}',
                    middle_name = '{_middle_name}',
                    last_name = '{_last_name}'
                WHERE user_id = {_user_id}
                RETURNING user_id
                """
        with psycopg2.connect(CONNECT_LINE) as conn:
            with TransactionCtx(conn) as transaction:
                with conn.cursor() as cursor:
                    cursor.execute(_SQL)

    def delete_user(self, _user_id) -> bool:
        """Удаляет объект user по указанному user_id"""
        _SQL = f"""
                DELETE FROM users
                WHERE user_id = {_user_id}
                """
        with psycopg2.connect(CONNECT_LINE) as conn:
            with TransactionCtx(conn) as transaction:
                with conn.cursor() as cursor:
                    cursor.execute(_SQL)
                    return True

        return False

    def data_to_dict(self, data: list) -> dict:
        """Перобразует объект список данных БД в словарь."""
        return {'user_id': data[0],
                'first_name': data[1],
                'middle_name': data[2],
                'last_name': data[3]}
