"""Models and functions for database"""
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import pytz

# This is the connection to the PostgreSQL database;
# We're getting this through the Flask_SQLAlchemy helper library;
# On this connection we can find the `session` object;
# Where we do most of our interactions like committing, etc.

# SQLAlchemy is a python library
# SQLAlchemy includes a db server and Object relational mapping (ORM)

#instantiates object that allows connection to db
db = SQLAlchemy()

###############################################################################
#Model definitions
class User(db.Model):
    """User account info"""
    __tablename__ = "users"

    user_id = db.Column(db.Integer, 
                        autoincrement=True, 
                        primary_key=True)
    fname = db.Column(db.String(64), nullable=False)
    lname = db.Column(db.String(64))
    username = db.Column(db.String(64), unique=True, nullable=False)
    password = db.Column(db.String(64), nullable=False)
    

    def __repr__(self):
        """Provide helpful representation when printed."""

        return "<user_id={user_id} first_name={fname} last_name={lname} \
                username={username} password={password}>".format(
                    user_id=self.user_id, fname=self.fname, lname=self.lname,
                    username=self.username, password=self.password) #pragma: no cover


class Type(db.Model):
    """Poop types"""

    __tablename__ = "types"

    type_id = db.Column(db.Integer, 
                        primary_key=True)
    type_name = db.Column(db.String(8), nullable=False)
    type_img = db.Column(db.String(64), nullable=True)  # <--- TODO: nullable=False
    type_description = db.Column(db.String(256), nullable=True) # <-- TODO: nullable=False

    def __repr__(self):

        return "<type_id={id} type_name={name} type_img={img} \
                type_description={description}>".format(id=self.type_id,
                name=self.type_name, img=self.type_img,
                description=self.type_description)  #pragma: no cover


class Event(db.Model):
    """User poop events"""

    __tablename__ = "events"

    event_id = db.Column(db.Integer, 
                            autoincrement=True,
                            primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    type_id = db.Column(db.Integer, db.ForeignKey('types.type_id'))
    event_at = db.Column(db.DateTime)
    comment = db.Column(db.String(256), default=None)

    user_event = db.relationship('User', backref="users") #backref gets all user info
    event_type = db.relationship('Type', backref="types") 

    def __repr__(self):

        return "<event_id={event_id} user_id={user_id} \
                    type_id={type_id} event_at={event_at} \
                        comment={comment}>".format(event_id=self.event_id,
                                user_id=self.user_id, type_id=self.type_id,
                                 event_at=self.event_at, comment=self.comment)  #pragma: no cover



#<---------------------------------------------------------------------------->

def example_data():
    """Create sample data"""

    Lauren = User(fname='Lauren', lname='Burwell', username='lburwell', 
                    password='lburwell')
    event_1 = Event(user_id=self.user_1.user_id, type_id=self.type_7.type_id, \
                         comment='lumpy, brown', event_at='2018-06-12')

    
    db.session.add(Lauren)
    db.session.commit()

#<---------------------------------------------------------------------------->
    # Helper functions

#passed 2 param, testing.py passes postgresql:///testdb
def connect_to_db(app, db_uri='postgresql:///dumps'):
    """Connect the databse to our Flask app"""

    #locaction of default db
    app.config['SQLALCHEMY_DATABASE_URI'] =  db_uri     
    
    #autosets to True
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False    
    
    #instantiates app; connects app to db 
    db.app = app       
    
    #make active connection
    db.init_app(app)    


if __name__ == '__main__':  #pragma: no cover
    # if you run this module interactively
    # you can work with the DB directly

    from server import app
    connect_to_db(app)
    print "Connected to DB."







