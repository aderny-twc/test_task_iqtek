import os

app_dir = os.path.abspath(os.path.dirname(__file__))


class BaseConfig:
    """Базовая конфигурация проекта."""
    SECREY_KEY = os.environ.get('SOME_SECRET_KEY') or 'A_DEFAULT_SECRET'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class MysqlDBConfig(BaseConfig):
    """Отладочная конфигурация, работающая с БД MySQL/MariaDB."""
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('MYSQL_DATABASE_URI') or 'mysql+pymysql://testAPI:testAPIpasswd@localhost/testAPIdb'


class SqliteDBConfig(BaseConfig):
    """Отладочная конфигурация, работающая с БД SqLite."""
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLITE_DATABASE_URI') or 'sqlite:////home/ando/python_code/test_flask_api_iqt/testAPIdb.db'
