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


class PostgreConfig(DBConfig):
    SQLALCHEMY_DATABASE_URI = (f"postgresql://{os.environ.get('username')}:"
                               f"{os.environ.get('password')}@{os.environ.get('host')}:"
                               f"{os.environ.get('port')}/{os.environ.get('database')}")


def get_config():
    if os.environ.get('ENV') == 'TEST':
        return TestConfig, PostgreConfig
    elif os.environ.get('ENV') == 'PROD':
        return ProdConfig, None
    else:
        return Config, None


if __name__ == '__main__':
    print(PostgreConfig.SQLALCHEMY_DATABASE_URI)
