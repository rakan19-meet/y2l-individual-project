from model import *

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///hotels.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def create_hotel(name, booking_date, description, price, photo):
    hotel_object = Hotel(
    	name = name,
    	booking_date = booking_date,
    	description = description,
    	price = price,
    	photo = photo
    )
    session.add(hotel_object)
    session.commit()

def get_all_hotels():
	hotels = session.query(Hotel).all()
	return hotels

def get_one_hotel(id):
	hotel = session.query(Hotel).filter_by(id = id).first()
	return hotel

# create_hotel('TEST 2', '23/01/2019-31/01/2019', "This is a test for the description of the hotel", 67685, "https://s-ec.bstatic.com/images/hotel/max1280x900/101/101430248.jpg")