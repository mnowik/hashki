import os

config = {
    "development": "config.config.DevelopmentConfig",
    "testing": "config.config.TestingConfig",
    "default": "config.config.DevelopmentConfig"
}


def configure_app(app):
    config_name = os.getenv('FLASK_CONFIGURATION', 'default')
    app.config.from_object(config[config_name])
    app.config.from_pyfile('config.cfg', silent=True)