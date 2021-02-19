from app.db.db_teller import DataBase


class MemoryDB(DataBase):
    """Репозиторий БД, хранящий объекты user"""
    _users = []

    def __init__(self):
        super().__init__()
        self.db_name = 'Memory Database'

    def add_user(self, _first_name, _middle_name, _last_name) -> None:
        """Создание нового объекта user c указанными полями."""
        if self._users:
            _user_id = self._users[-1]['user_id'] + 1
        else:
            _user_id = 1
        new_user = {
            'user_id': _user_id,
            'first_name': _first_name,
            'middle_name': _middle_name,
            'last_name': _last_name,
        }
        self._users.append(new_user)

    def get_user(self, _user_id):
        """Возвращает объект пользователя с указанным user_id."""
        place = self.find_place_user(_user_id)
        if place is not None:
            return self._users[place]

    def update_user(self, _user_id, _first_name, _middle_name, _last_name) -> None:
        """Обновляет указанные данные объекта user по user_id"""
        place = self.find_place_user(_user_id)

        if place is not None:
            self._users[place]['first_name'] = _first_name
            self._users[place]['middle_name'] = _middle_name
            self._users[place]['last_name'] = _last_name

    def delete_user(self, _user_id) -> bool:
        """Удаляет объект user по указанному user_id"""
        place = self.find_place_user(_user_id)

        if place is not None:
            self._users.pop(place)
            return True

    def find_place_user(self, _user_id) -> int:
        """Поиск объекта user по user_id."""
        for num, user in enumerate(self._users, start=0):
            # Проверка наличия user с указанным user_id
            if user['user_id'] == _user_id:
                return num
