# from sqlalchemy import func
from model import User, Event, Type, connect_to_db, db
import datetime
from server import app

class Seed_Data(object):
    
    def __init__(self):
        Event.query.delete()
        User.query.delete()     #if running multiple times, delete to avoid dup 
        Type.query.delete()
        
        self.user_1 = User(fname='Lauren', lname='Burwell', \
                            username='lburwell', password='lburwell')                
        self.user_2 = User(fname='Jess', lname='Kos', \
                            username='jkos', password='jkos')
        self.user_3 = User(fname='Melvin', lname='Mitchell', \
                            username='mmitchell', password='mmitchell')
        self.user_4 = User(fname='Naa', lname='Badger', \
                            username='nbadger', password='nbadger')

        self.type_1 = Type(type_id=1, type_name='Type 1', \
                            type_description='Indicates constipation',
                                type_img='/static/poopimages/t1.png')
        self.type_2 = Type(type_id=2, type_name='Type 2', \
                            type_description='Indicates constipation',
                                type_img='/static/poopimages/t2.png')
        self.type_3 = Type(type_id=3, type_name='Type 3', \
                            type_description='Considered normal or ideal',
                                type_img='/static/poopimages/t3.png')
        self.type_4 = Type(type_id=4, type_name='Type 4', \
                            type_description='Considered normal or ideal',
                                type_img='/static/poopimages/t4.png')
        self.type_5 = Type(type_id=5, type_name='Type 5', \
                            type_description='Indicates diarrhea',
                                type_img='/static/poopimages/t5.png')
        self.type_6 = Type(type_id=6, type_name='Type 6', \
                            type_description='Indicates diarrhea',
                                type_img='/static/poopimages/t6.png')
        self.type_7 = Type(type_id=7, type_name='Type 7', \
                            type_description='Indicates diarrhea',
                                type_img='/static/poopimages/t7.png')

        db.session.add_all([self.user_1, self.user_2, self.user_3, self.user_4, \
                        self.type_1, self.type_2, self.type_3, self.type_4, \
                        self.type_4, self.type_5, self.type_6, self.type_7]) 
        db.session.commit()


    def event_data(self):

        event_1 = Event(user_id=self.user_1.user_id, type_id=self.type_1.type_id, \
                         comment='lumpy, brown', event_at='2018-01-24')
        event_2 = Event(user_id=self.user_1.user_id, type_id=self.type_3.type_id, \
                        comment='long, hard to pass', event_at='2018-03-11')
        event_3 = Event(user_id=self.user_2.user_id, type_id=self.type_6.type_id, \
                        comment='very light brown', event_at='2018-05-14')
        event_4 = Event(user_id=self.user_3.user_id, type_id=self.type_1.type_id, \
                        comment='lumpy, brown', event_at='2018-02-22')
        
        db.session.add_all([event_1, event_2, event_3, event_4])
        db.session.commit()




if __name__ == "__main__":
    connect_to_db(app)

    #create tables
    db.create_all()

    #create instance (seed_data) on class (Seed_Data()) and call
    #call event_data() method on instance
    seed_data = Seed_Data()        
    seed_data.event_data()




