import os

class Config:

    NEWS_API_BASE_URL ='https://newsapi.org/{}?api_key={}'
    SOURCES_BASE_URL = 'https://newsapi.org/v2/sources{}?api_key={}'
    EVERYTHING_SOURCE_BASE_URL = 'https://newsapi.org/v2/everything/{}?api_key={}' 
    EVERYTHING_BASE_URL = 'https://newsapi.org/v2/everything/{}?api_key={}' 
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')


class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}