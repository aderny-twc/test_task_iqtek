from injector import singleton

from .db_teller import DBService, DataBase
from .sql_rep import PostgresDB
from .mem_rep import MemoryDB


def configure(binder):
    binder.bind(DBService, to=DBService, scope=singleton)
    binder.bind(DataBase, to=MemoryDB, scope=singleton)
    binder.bind(DataBase, to=PostgresDB, scope=singleton)

