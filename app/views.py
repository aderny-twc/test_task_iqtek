from app import app
from flask import request, jsonify, make_response, abort
from flask_injector import FlaskInjector
from injector import inject

from .db.db_teller import DBService
from .db.dependencies import configure


@inject
@app.route('/test/api/v0.1/user/<int:user_id>/', methods=['GET'])
def get_user(user_id, service: DBService):
    """Получение объекта пользователя по user_id."""
    print(f"MyService instance is {service}")
    getting_user = service.get_user(user_id)
    if getting_user:
        return jsonify(getting_user)
    else:
        abort(404)


@inject
@app.route('/test/api/v0.1/user/', methods=['POST'])
def create_user(service: DBService):
    """Создание нового объекта пользователя."""
    if input_validation(request.json):
        service.add_user(request.json['first_name'],
                         request.json['middle_name'],
                         request.json['last_name'])

    resp_body = jsonify({'Response': 'User created'})
    return make_response(resp_body, 201)


@inject
@app.route('/test/api/v0.1/user/<int:user_id>/', methods=['PUT'])
def update_user(user_id, service: DBService):
    """Обновление объекта пользователя с user_id."""
    if input_validation(request.json):
        service.update_user(user_id,
                            request.json['first_name'],
                            request.json['middle_name'],
                            request.json['last_name'])

    resp_body = jsonify({'Response': 'User updated'})
    return make_response(resp_body, 200)


@inject
@app.route('/test/api/v0.1/user/<int:user_id>/', methods=['DELETE'])
def delete_user(user_id, service: DBService):
    """Удаление объекта пользователя c user_id."""
    if service.delete_user(user_id):
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


# Setup Flask Injector
FlaskInjector(app=app, modules=[configure])
