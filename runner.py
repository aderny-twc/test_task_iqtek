from app import app
from flask_script import Manager, Shell


manager = Manager(app)

manager.add_command('shell', Shell())

if __name__ == '__main__':
    manager.run()