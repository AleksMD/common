import os


class Config:
    DEBUG = False
    SECRET_KEY = 'secret'


class TestConfig(Config):
    SECRET_KEY = 'Test'
    DEBUG = True


class ProdConfig(Config):
    SECRET_KEY = 'Prod'


def get_config():
    if os.environ.get('ENV') == 'TEST':
        return TestConfig
    elif os.environ.get('ENV') == 'PROD':
        return ProdConfig
    else:
        return Config
