import os
from app import app, db
from app.models import User
from flask_script import Manager, Shell


manager = Manager(app)


def make_shell_context():
    """Задает переменные для доступа внутри оболочки."""
    return dict(app=app, db=db, User=User)


manager.add_command('shell', Shell(make_context=make_shell_context))


if __name__ == '__main__':
    manager.run()

