from abc import ABC, abstractmethod


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
    """Фабрика объектов реализаций БД."""

    def __init__(self, db: DataBase):
        """Определение типа БД."""
        self.db = db

    def create_db(self) -> DataBase:
        """Возвращает объект БД."""
        return self.db()
