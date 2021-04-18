import MySQLdb
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from config import Config

engine = create_engine(Config.SQLALCHEMY_DATABASE_URI, echo=False, future=True)
Session = sessionmaker(bind=engine)
db = Session()
connection = MySQLdb.connect(host='localhost', database='auto_park', user='root', password='vecrekflvsy', charset='utf8mb4')
cursor = connection.cursor()