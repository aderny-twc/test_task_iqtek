from flask import Flask
import os


# Создание экземпляра приложения
app = Flask(__name__)
# Выбор конфигурации
app.config.from_object(os.environ.get('FLASK_ENV') or 'config.MemoryDBConfig')


# Импорт views
from . import views
