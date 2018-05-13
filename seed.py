# from sqlalchemy import func
from model import User, Event, Type, connect_to_db, db
import datetime
from server import app

class Seed_Data(object):

    User.query.delete()     #if running multiple times, delete to avoid dup 
    Type.query.delete()
    
    def __init__(self):
        self.user_1 = User(fname='Lauren', lname='Burwell', username='lburwell', password='lburwell')                
        self.user_2 = User(fname='Jess', lname='Koss', username='jkoss', password='jkoss')
        self.user_3 = User(fname='Melvin', lname='Mitchell', username='mmitchell', password='mmitchell')
        self.user_4 = User(fname='Naa', lname='Badger', username='nbadger', password='nbadger')

        self.type_1 = Type(type_name='Type 1', type_description='this is type 1')
        self.type_2 = Type(type_name='Type 2', type_description='this is type 2')
        self.type_3 = Type(type_name='Type 3', type_description='this is type 3')
        self.type_4 = Type(type_name='Type 4', type_description='this is type 4')
        self.type_5 = Type(type_name='Type 5', type_description='this is type 5')
        self.type_6 = Type(type_name='Type 6', type_description='this is type 6')
        self.type_7 = Type(type_name='Type 7', type_description='this is type 7')

        db.session.add_all([self.user_1, self.user_2, self.user_3, self.user_4, \
                        self.type_1, self.type_2, self.type_3, self.type_4, \
                        self.type_4, self.type_5, self.type_6, self.type_7]) 
        db.session.commit()


    def event_data(self):

        Event.query.delete()

        event_1 = Event(user_id=self.user_1.user_id, type_id=self.type_1.type_id, comment='hard balls')
        event_2 = Event(user_id=self.user_1.user_id, type_id=self.type_3.type_id, comment='sausage-shaped, cracks')
        event_3 = Event(user_id=self.user_2.user_id, type_id=self.type_6.type_id, comment='fluffy pieces')
        event_4 = Event(user_id=self.user_3.user_id, type_id=self.type_1.type_id, comment='hard balls')
        
        db.session.add_all([event_1, event_2, event_3, event_4])
        db.session.commit()




if __name__ == "__main__":
    connect_to_db(app)

    #create tables
    db.create_all()

    #import User, Type, Event data 
    # seed_data = Seed_Data()        
    # event_data()




