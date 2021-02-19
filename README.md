# Flask REST API интерфейс
API интерфейс, реализующий операции над сущностью User

## Поля модели

| Поле        | Тип     |
| ----------- | ------- |
| user_id     | int     |
| first_name  | varchar |
| middle_name | varchar |
| last_name   | varchar |

## views

| Путь                               | Метод  | Действие              |
| ---------------------------------- | ------ | --------------------- |
| /test/api/v0.1/user/<int:user_id>/ | GET    | Получение user по id  |
| /test/api/v0.1/user/               | POST   | Создание user         |
| /test/api/v0.1/user/<int:user_id>/ | PUT    | Обновление user по id |
| /test/api/v0.1/user/<int:user_id>/ | DELETE | Удаление user по id   |

## Структура проекта

```
user_test_api_iqt/
├── app
│   ├── db
│   │   ├── db_teller.py
│   │   ├── __init__.py
│   │   ├── mem_rep.py
│   │   ├── sql_rep.py
│   │   └── transactioncm.py
│   ├── __init__.py
│   └── views.py
├── config.py
├── README.md
└── runner.py
```

## Запуск сервиса

### Загрузка проекта

```
git clone https://github.com/aderny-twc/user_test_api_iqt.git
cd user_test_api_iqt
```

### Установка зависимостей

```
(venv) $ pip install -r requirements.txt
```

Для смены конфигурации репозитория нужно создать переменную среды `FLASK_ENV`. Доступные конфигурации: `config.PostgresDBConfig` или `config.MemoryDBConfig`.

Для Mac/Linux переменная среды `FLASK_ENV`:

```
(venv) $ export FLASK_ENV=config.PostgresDBConfig
```

Для Windows переменная среды `FLASK_ENV`:

```
(venv) > set FLASK_ENV=config.PostgresDBConfig
```

### Запуск

```
$ python runner.py runserver
```

