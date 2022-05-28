class Config:
    SECRET_KEY = 't5s~}\9u?ED{^U9Yñ'


class DevelopmentConfig(Config):
    DEBUG = True
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = 'Zamudio_3108'
    MYSQL_DB = 'checky'


config = {
    'development': DevelopmentConfig
}