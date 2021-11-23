from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from app.config import Config

engine = create_engine(url=Config.get_base_config())
# engine = create_engine(url=Config.get_test_config())

Base = declarative_base()
# Session = sessionmaker()
# Session.configure(bind=engine)
# session = Session()

# a little more clear
session_maker = sessionmaker()
session_maker.configure(bind=engine)
session = session_maker()
