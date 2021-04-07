import os


class Config(object):
    SQLALCHEMY_LOCAL_URI = 'mysql+mysqlconnector://root:vecrekflvsy@172.16.2.15/auto_park'
    SQLALCHEMY_DATABASE_URI = os.environ.get('CLEARDB_PUCE_URL') or SQLALCHEMY_LOCAL_URI
    SQLALCHEMY_TRACK_MODIFICATIONS = False