# Clase maestra Config
class Config:
    SECRET_KEY = 't5s~}\9u?ED{^U9Yñ'

# Clase para configuraciones de desarrollo que hereda de clase Config
class DevelopmentConfig(Config):
    DEBUG = True
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = 'Zamudio_3108'
    MYSQL_DB = 'checky'

# Diccionario config que instancia a las configuraciones de desarrollo
config = {
    'development': DevelopmentConfig
}