import os

basedir = os.path.abspath(os.path.dirname(__file__))

class FrontendConfig(object):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///'+ os.path.join(basedir,'frontend_app.db')
    SECRET_KEY = os.environ.get('SECRET_KEY')
    DEBUG = True

class AdminConfig(object):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///'+ os.path.join(basedir,'admin_app.db')
    SECRET_KEY = os.environ.get('SECRET_KEY')
    DEBUG = True