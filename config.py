import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///'+ os.path.join(basedir,'frontend_app.db')
    # SQLALCHEMY_DATABASE_URI = 'sqlite///frontend_app.db'
    SECRET_KEY = os.environ.get('SECRET_KEY')
    DEBUG = True 