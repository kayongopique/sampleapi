import os


class Config(object):
    """Parent configuration class."""
    DEBUG = False
    CSRF_ENABLED = True
    SECRET = os.getenv('SECRET') or "huge string"
    DATABASE_URI = os.getenv('DATABASE_URL')


class DevelopmentConfig(Config):
    """Configurations for Development."""
    DEBUG = True
    DATABASE_URL = 'postgres://postgres:david@localhost:5432/api_db'


class TestingConfig(Config):
    """Configurations for Testing, with a separate test database."""
    TESTING = True
    DATABASE_URI = 'postgres://postgres:david@localhost:5432/testapi_db'
    DEBUG = True


app_config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
}
