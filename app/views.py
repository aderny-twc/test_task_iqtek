from app import app
from flask import request
from .models import User


@app.route('/test/api/v0.1/user/<int:user_id>/', methods=['GET'])
def get_user(user_id):
    """Получение объекта пользователя по user_id."""
    pass


@app.route('/test/api/v0.1/user/', methods=['POST'])
def create_user():
    """Создание нового объекта пользователя."""
    pass


@app.route('/test/api/v0.1/user/<int:user_id>/', methods=['PUT'])
def update_user(user_id):
    """Обновление объекта пользователя с user_id."""
    pass


@app.route('/test/api/v0.1/user/<int:user_id>/', methods=['DELETE'])
def delete_user(user_id):
    """Удаление объекта пользователя c user_id."""
    pass

