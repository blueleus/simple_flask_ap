import os


class Config(object):
    DEBUG = True
    DEVELOPMENT = True
    SECRET_KEY = 'dev1'
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{os.path.join(os.path.dirname(os.path.abspath(__file__)), "flask.sqlite")}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
