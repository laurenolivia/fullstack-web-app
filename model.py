"""Models and functions for database"""
from flask_sqlalchemy import SQLAlchemy

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
    events = db.relationship('Events', backref='user') # <-- is this right?

    def __repr__(self):
        """Provide helpful representation when printed."""

        return "<user_id={user_id} first_name={fname} last_name={lname} \
                username={username} password={password}>".format(
                    user_id=self.user_id, fname=self.fname, lname=self.lname,
                    username=self.username, password=self.password)

class Type(db.Model):
    """Poop types"""

    __tablename__ = "types"

    type_id = db.Column(db.Integer, 
                        autoincrement=True, #should this autoincrement?
                        primary_key=True)
    type_name = db.Column(db.String(8), nullable=False)
    type_img = db.Column(db.LargeBinary, nullable=False)  # <--- what datatype?
    type_description = db.Column(db.String(256), nullable=False)

    def __repr__(self):

        return "<type_id={id} type_name={name} type_img={img} \
                type_description={description}>".format(id=self.type_id,
                name=self.type_name, img=self.type_img,
                description=self.type_description)

class Event(db.Model):
    """User poop events"""

    __tablename__ = "events"

    event_id = db.Column(db.Integer, 
                            autoincrement=True,
                            primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    type_id = db.Column(db.Integer, db.ForeignKey('types.type_id'))
    event_at = db.Column(db.DateTime)
    comment = db.Column(db.String(256))

#<---------------------------------------------------------------------------->
    # Helper functions

def connect_to_db(app):
    """Connect the databse to our Flask app"""

    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///dumps' #locaction of db
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False #autosets to True
    db.app = app    #instantiates app; connects app to db    
    db.init_app(app)    #make active connection


if __name__ == '__main__':
    # if you run this module interactively
    # you can work with the DB directly

    from server import app
    connect_to_db(app)
    print "Connected to DB."







