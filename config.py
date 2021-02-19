import os
#from app.db.sql_rep import PostgresDB
from app.db.mem_rep import MemoryDB

app_dir = os.path.abspath(os.path.dirname(__file__))


class BaseConfig:
    """Базовая конфигурация проекта."""
    SECRET_KEY = os.environ.get('SOME_SECRET_KEY') or 'A_DEFAULT_SECRET'


#class PostgresDBConfig(BaseConfig):
#    """Отладочная конфигурация, работающая с PostgreSQL."""
#    DEBUG = True
#    CONNECT_LINE = os.environ.get('POSTGRES_DATABASE_URI') or 'postgres://testapi:testAPIpasswd@localhost/testapidb'
#    DEFAULT_DATABASE = PostgresDB


class MemoryDBConfig(BaseConfig):
    """Отладочная конфигурация, сохраняющая данные в памяти."""
    DEBUG = True
    DEFAULT_DATABASE = MemoryDB
