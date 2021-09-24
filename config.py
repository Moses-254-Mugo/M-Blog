import os
class Config:
    '''
    General configuration parent class
    '''
    pass
class ProdConfig(Config):
    '''
    Production  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass
class TestConfig(Config):
    pass
class DevConfig(Config):
    '''
    Development  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig
}