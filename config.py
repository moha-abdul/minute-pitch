import os

class Config:
    pass
    # SECRET_KEY = os.environ.get('SECRET_KEY')

class ProdConfig(Config):
    pass


class DevConfig(Config):
    pass

# config_options = {
# 'development':DevConfig,
# 'production':ProdConfig
# }