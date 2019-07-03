from app import create_app,db
from flask_script import Manager,Server
from app.models import Group
from flask_migrate import Migrate,MigrateCommand
import os

app = create_app('production')
SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://francis:1234@localhost/nlist' 

# Create manager instance 
manager = Manager(app)

# Create migrate instance
migrate = Migrate(app,db)

manager.add_command('server',Server)
manager.add_command('db',MigrateCommand)

@manager.command
def test():
    '''
    Run the unit tests
    '''
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)


@manager.shell
def make_shell_context():
    return dict( app=app, db=db, Group=Group)


if __name__ == '__main__':
    manager.run()