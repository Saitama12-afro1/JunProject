class Config(object):
    DEBUG = True
    TESTING = False
    SECRET_KEY = "12121212121"
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:danila2001@localhost:5432/juntest"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    

class Url_sait(object):
    url = "https://jservice.io/api/random?"
