import os
class Config:
    SECRET_KEY = '1234'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://francis:1234@localhost/nlist'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOADED_PHOTOS_DEST ='app/static/photos'
   
    
    
#  email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME='mukuha58@gmail.com'
    MAIL_PASSWORD='fwm284fwm'

 
class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
class TestConfig(Config):
    '''
    Testing configuration child class
    Args:
        Config: The parent configuration class with General configuration settings 
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://francis:1234@localhost/nlist'

class DevConfig(Config):
    '''
    Development configuration child class
    
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://francis:1234@localhost/nlist'

    DEBUG = True


config_options = {
    'development': DevConfig,
    'production': ProdConfig,
    'test': TestConfig
}
# DATABASE_URL:  postgres://wwievyfpmoxelu:9a1da47c876ca17241c83c5d2062ba2ef22f9cabd49dc5220ae9964f41c1d249@ec2-54-243-47-196.compute-1.amazonaws.com:5432/da2l6r2rcmj5sj