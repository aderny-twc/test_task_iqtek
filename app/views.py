from app import app
from flask import request, jsonify, make_response
from .models import User


@app.route('/test/api/v0.1/user/<int:user_id>/', methods=['GET'])
def get_user(user_id):
    """Получение объекта пользователя по user_id."""
    getting_user = User.get_user(user_id)
    return jsonify(getting_user)


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


#Возвращение ошибки при отстутствии данных
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not Found'}), 404)


def input_validation(json_obj):
    """
    Проверка входных данных. Принимает объект json.
    """
    user_fields = ['first_name', 'middle_name', 'last_name']
    for field in user_fields:
        if (field in json_obj
            and type(json_obj[field]) != unicode):
            abort(400)


