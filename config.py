import os


basedir = os.path.abspath(os.path.dirname(__file__))

class Configuration:
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'postgres+psycopg2://postgres:@db:5432/postgres' #'sqlite:///' + os.path.join(basedir, 'app.db')
    SECRET_KEY = "mysecertkey"

    ###flask_security
    SECURITY_PASSWORD_SALT = "salt"
    SECURITY_PASSWORD_HASH = "sha512_crypt"
