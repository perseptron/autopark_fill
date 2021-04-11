import os


class Config(object):
    SQLALCHEMY_LOCAL_URI = 'mysql+mysqldb://root:vecrekflvsy@127.0.0.1/auto_park?charset=utf8mb4'
    SQLALCHEMY_DATABASE_URI = os.environ.get('CLEARDB_PUCE_URL') or SQLALCHEMY_LOCAL_URI
    SQLALCHEMY_TRACK_MODIFICATIONS = False