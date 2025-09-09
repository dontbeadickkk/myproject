import os

class Config(object):
    USER = os.environ.get('POSTGRES_USER', 'ntk')
    PASSWORD = os.environ.get('POSTGRES_PASSWORD', 'ntk2004')
    HOST = os.environ.get('POSTGRES_HOST', '127.0.0.1')
    PORT = os.environ.get('POSTGRES_PORT', 5532)
    DB= os.environ.get('POSTGRES_DB', 'mydb')

    SQLALCHEMY_DATABASE_URI = f'postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB}'
    SECRET_KEY = 'eRxMATbuzpCdrKMA5hMQZNGeVkpRKX6e'
    SQLALCHEMY_TRACK_MODIFICATIONS = True