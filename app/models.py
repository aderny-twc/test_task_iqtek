from app import db
import json


class User(db.Model):
    """Модель пользователя."""
    __tablename__ = 'users'
    user_id = db.Column(db.Integer(), primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    middle_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)

    def add_user(_first_name, _middle_name, _last_name):
        """Метод для создания нового пользователя."""
        new_user = User(first_name=_first_name,
                        middle_name=_middle_name,
                        last_name=_last_name,)
        db.session.add(new_user)
        db.session.commit()
        return new_user

    def get_user(_user_id):
        """Возвращает объект пользователя по user_id."""
        getting_user = User.query.get_or_404(_user_id)
        return getting_user

    def update_user(_user_id, _first_name, _middle_name, _last_name):
        upd_fields = {'first_name': _first_name,
                        'middle_name': _middle_name,
                        'last_name': _last_name,}
        upd_user = User.query.filter_by(user_id=_user_id).update(upd_fields)
        db.session.commit()


    def __repr__(self):
        """Отображение пользователя в shell."""
        user_obj = {
                'user_id': self.user_id,
                'first_name': self.first_name,
                'middle_name': self.middle_name,
                'last_name': self.last_name,
                }
        return json.dumps(user_obj)


