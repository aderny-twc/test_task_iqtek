from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

# Создание экземпляра приложения
app = Flask(__name__)
# Выбор конфигурации
app.config.from_object(os.environ.get('FLASK_ENV') or 'config.SqliteDBConfig')

# Инициализация расширений
db = SQLAlchemy(app)

# Импорт views
from . import views
