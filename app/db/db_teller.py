from abc import ABC, abstractmethod
from injector import inject


class DataBase(ABC):
    """Абстрактный родительский класс, определяющий методы общения с БД."""

    def __init__(self):
        pass

    @abstractmethod
    def add_user(self):
        pass

    @abstractmethod
    def get_user(self):
        pass

    @abstractmethod
    def update_user(self):
        pass

    @abstractmethod
    def delete_user(self):
        pass


class DBService:
    """Сервис общения с БД."""
    @inject
    def __init__(self, db: DataBase):
        """Определение типа БД."""
        self.db = db

    def add_user(self, _first_name, _middle_name, _last_name):
        return self.db.add_user(_first_name, _middle_name, _last_name)

    def get_user(self, user_id):
        return self.db.get_user(user_id)

    def update_user(self, user_id, _first_name, _middle_name, _last_name):
        return self.db.update_user(user_id, _first_name, _middle_name, _last_name)

    def delete_user(self, user_id):
        return self.db.delete_user(user_id)

