from model import User, Event, Type, connect_to_db, db
# from flask_sqlalchemy import SQLAlchemy 
from server import app
import datetime


def seed_data():

    user_1 = User(fname='Lauren', lname='Burwell', username='lburwell', password='lburwell')                
    user_2 = User(fname='Jess', lname='Koss', username='jkoss', password='jkoss')
    user_3 = User(fname='Melvin', lname='Mitchell', username='mmitchell', password='mmitchell')
    user_4 = User(fname='Naa', lname='Badger', username='nbadger', password='nbadger')

    type_1 = Type(type_name='Type 1', type_description='this is type 1')
    type_2 = Type(type_name='Type 2', type_description='this is type 2')
    type_3 = Type(type_name='Type 3', type_description='this is type 3')
    type_4 = Type(type_name='Type 4', type_description='this is type 4')
    type_5 = Type(type_name='Type 5', type_description='this is type 5')
    type_6 = Type(type_name='Type 6', type_description='this is type 6')
    type_7 = Type(type_name='Type 7', type_description='this is type 7')

    event_1 = Event(user_event=user_1, event_type=type_1, comment='hard balls')
    event_2 = Event(user_event=user_1, event_type=type_3, comment='sausage-shaped, cracks')
    event_3 = Event(user_event=user_2, event_type=type_6, comment='fluffy pieces')
    event_4 = Event(user_event=user_3, event_type=type_1, comment='hard balls')
    



    db.session.add_all([user_1, user_2, user_3, user_4, \
                    type_1, type_2, type_3, type_4, \
                    type_4, type_5, type_6, type_7, \
                    event_1, event_2, event_3, event_4])
    
    db.session.commit()



# error no flask_sqlalchemy found line 2 model
# recreated virtualenv which deletes everything I pip installed

#how to populate events table since it has two foreign keys

# and relationships with two tables