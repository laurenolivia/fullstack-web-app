# from sqlalchemy import func
from model import User, Event, Type, connect_to_db, db
import datetime
from server import app

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

    db.session.add_all([user_1, user_2, user_3, user_4, \
                    type_1, type_2, type_3, type_4, \
                    type_4, type_5, type_6, type_7,]) 
    db.session.commit()                    
        
    def event_data():

        event_1 = Event(user_id=user_1.user_id, type_id=type_1.type_id, comment='hard balls')
        event_2 = Event(user_id=user_1_user_id, type_id=type_3.type_id, comment='sausage-shaped, cracks')
        event_3 = Event(user_id=user_2.user_id, type_id=type_6.type_id, comment='fluffy pieces')
        event_4 = Event(user_id=user_3.user_id, type_id=type_1.type_id, comment='hard balls')
        
        db.session.add_all([event_1, event_2, event_3, event_4])
        db.session.commit()




if __name__ = "__main__":
    connect_to_db(app)

    #create tables
    db.create_all()

    #import data 
    seed_data()        




