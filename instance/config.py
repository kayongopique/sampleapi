import os


class Config(object):
    """Parent configuration class."""
    DEBUG = False
    CSRF_ENABLED = True
    SECRET = os.getenv('SECRET') or "huge string"
    DATABASE_URI = os.getenv('DATABASE_URL')
    CORS_ORIGIN_WHITELIST = [
        'http://localhost:3000',
        'http://0.0.0.0:3000',
        'http://0.0.0.0:4100',
        'http://localhost:4100',
        'http://0.0.0.0:8000',
        'http://localhost:8000',
        'http://0.0.0.0:4200',
        'http://localhost:4200',
        'http://0.0.0.0:4000',
        'http://localhost:4000',
        'http://localhost:5000',
    ]


class DevelopmentConfig(Config):
    """Configurations for Development."""
    DEBUG = True
    DATABASE_URL = 'postgres://postgres:david@localhost:5432/api_db?stringtype=unspecified'


class TestingConfig(Config):
    """Configurations for Testing, with a separate test database."""
    TESTING = True
    DATABASE_URI = 'postgres://postgres:david@localhost:5432/testapi_db?stringtype=unspecified'
    DEBUG = True


class ProductionConfig(Config):
    """Configurations for Production."""
    DATABASE_URI = os.getenv('DATABASE_URL')


app_config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
}
