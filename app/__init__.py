from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from config import Config

engine = create_engine(Config.SQLALCHEMY_DATABASE_URI, echo=False, future=True)
Session = sessionmaker(bind=engine)
db = Session()
