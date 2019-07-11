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
    DATABASE_URL = os.getenv('DATABASE_URL') or 'postgres://postgres:david@localhost:5432/api_db'


class TestingConfig(Config):
    """Configurations for Testing, with a separate test database."""
    TESTING = True
    DATABASE_URI = 'postgres://postgres:david@localhost:5432/testapi_db'
    DEBUG = True


class ProductionConfig(Config):
    """Configurations for Production."""
    DATABASE_URI = os.getenv('DATABASE_URL')


app_config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
}
