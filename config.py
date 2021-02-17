import os

app_dir = os.path.abspath(os.path.dirname(__file__))


class BaseConfig:
    """Базовая конфигурация проекта."""
    SECRET_KEY = os.environ.get('SOME_SECRET_KEY') or 'A_DEFAULT_SECRET'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class PostgresDBConfig(BaseConfig):
    """Отладочная конфигурация, работающая с PostgreSQL."""
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('POSTGRES_DATABASE_URI') or 'postgresql+psycopg2://testapi:testAPIpasswd@localhost/testapidb'


class SqliteDBConfig(BaseConfig):
    """Отладочная конфигурация, работающая с БД SqLite."""
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLITE_DATABASE_URI') or "sqlite:///{}".format(os.path.join(app_dir, "flask-api.db"))
