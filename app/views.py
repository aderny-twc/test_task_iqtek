from app import app
from flask import request, jsonify, make_response, abort

from .db.db_teller import DBService

# Инициализация сервиса работы с БД - создание объекта класса.
db_service = DBService(app.config['DEFAULT_DATABASE']).create_db()


@app.route('/test/api/v0.1/user/<int:user_id>/', methods=['GET'])
def get_user(user_id):
    """Получение объекта пользователя по user_id."""
    getting_user = db_service.get_user(user_id)
    if getting_user:
        return jsonify(getting_user)
    else:
        abort(404)


@app.route('/test/api/v0.1/user/', methods=['POST'])
def create_user():
    """Создание нового объекта пользователя."""
    if input_validation(request.json):
        db_service.add_user(request.json['first_name'],
                            request.json['middle_name'],
                            request.json['last_name'])

    resp_body = jsonify({'Response': 'User created'})
    return make_response(resp_body, 201)


@app.route('/test/api/v0.1/user/<int:user_id>/', methods=['PUT'])
def update_user(user_id):
    """Обновление объекта пользователя с user_id."""
    if input_validation(request.json):
        db_service.update_user(user_id,
                               request.json['first_name'],
                               request.json['middle_name'],
                               request.json['last_name'])

    resp_body = jsonify({'Response': 'User updated'})
    return make_response(resp_body, 200)


@app.route('/test/api/v0.1/user/<int:user_id>/', methods=['DELETE'])
def delete_user(user_id):
    """Удаление объекта пользователя c user_id."""
    if db_service.delete_user(user_id):
        return jsonify({'Response': 'User deleted'})
    else:
        abort(404)


# Возвращение ошибки при отстутствии данных в БД
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not Found'}), 404)


# Возвращение ошибки недопустимого метода
@app.errorhandler(405)
def ivalid_mehtod(error):
    return make_response(jsonify({'error': 'Method Not Allowed'}), 405)


# Возвращение ошибки отсутсвия данных, неверных полях в теле запроса
@app.errorhandler(400)
def bad_request(error):
    return make_response(jsonify({'error': 'Empty data/invalid fields'}), 400)


def input_validation(json_obj):
    """
    Проверка входных данных. Принимает объект json.
    """
    user_fields = ['first_name', 'middle_name', 'last_name']
    for field in user_fields:
        if (field in json_obj
                and isinstance(json_obj[field], str)):
            continue
        else:
            abort(400)
    return True
