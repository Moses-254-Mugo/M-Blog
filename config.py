import os
class Config:
    '''
    General configuration parent class
    '''
    SECRET_KEY='kerugoya12'
    SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://moringa:Access@localhost/blog'
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    # MAIL_USERNAME='moseskinyua12@gmail.com'
    # MAIL_PASSWORD='kerugoya12'
    


    # simple mde  configurations
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True


    #  email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    

class ProdConfig(Config):
    '''
    Production  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    pass
class TestConfig(Config):
    pass
class DevConfig(Config):
    '''
    Development  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:Access@localhost/blog'


config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig
}