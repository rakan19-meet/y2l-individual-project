from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

# Write your classes here :
class Hotel(Base):
    __tablename__ = "hotels"
    id = Column(Integer, primary_key = True)
    name = Column(String)
    booking_date = Column(String)
    description = Column(String)
    price = Column(Integer)
    photo = Column(String)
