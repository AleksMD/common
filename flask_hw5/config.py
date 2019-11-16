import os


class Config:
    DEBUG = False
    SECRET_KEY = 'secret'


class TestConfig(Config):
    SECRET_KEY = 'Test'
    DEBUG = True


class ProdConfig(Config):
    SECRET_KEY = 'Prod'


class DBConfig:
    SQLALCHEMY_DATABASE_URI = None


class AppConfigTest(DBConfig, TestConfig):
    USERNAME = 'cursor'
    PASSWORD = os.environ.get('password')
    HOST = 'localhost'
    PORT = 5432
    DATABASE = 'cursor_db'
    SQLALCHEMY_DATABASE_URI = (f"postgresql://{USERNAME}:"
                               f"{PASSWORD}@{HOST}:"
                               f"{PORT}/{DATABASE}")


class AppConfigProd(DBConfig, ProdConfig):
    SQLALCHEMY_DATABASE_URI = (f"postgresql://{os.environ.get('username')}:"
                               f"{os.environ.get('password')}@{os.environ.get('host')}:"
                               f"{os.environ.get('port')}/{os.environ.get('database')}")


def get_config():
    if os.environ.get('ENV') == 'TEST':
        return AppConfigTest
    elif os.environ.get('ENV') == 'PROD':
        return AppConfigProd
    else:
        return Config
