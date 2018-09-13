import os

class Config:
    #SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://maxa:maxa12345@localhost/pitches'
    SECRET_KEY = os.environ.get('SECRET_KEY')
    '''
     the destination to store images
    '''
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    #  email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True

class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("HEROKU_POSTGRESQL_MAROON_URL")

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://maxa:maxa12345@localhost/pitches'

    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}