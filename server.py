from jinja2 import StrictUndefined
from flask import (Flask, render_template, 
                    redirect, request, session, flash, jsonify)
from flask_debugtoolbar import DebugToolbarExtension
from model import User, Type, Event, connect_to_db, db 
import datetime
import pytz

app = Flask(__name__)

app.secret_key = "thisisasecret"

#raise an error if jinja attributes don't exist
app.jinja_env.undefined = StrictUndefined  

@app.route('/home')
def index():
    """Homepage"""

    #display homepage with two buttons
    #register btn routes to /register page
    #login btn routes to /login
    return render_template('homepage.html')


@app.route('/register')
def register_form():
    """Requests username, password"""

    #render page with form
    #GET data and send to /validate_registration
    return render_template('register.html')

@app.route("/validate_registration", methods=["POST"])
def validate_registration():
    """Validate user and new user to db"""
    print request.form

    first_name = request.form.get("First")
    last_name = request.form.get("Last")
    username = request.form.get("Username")
    password = request.form.get("Password")

    #query for username in db, return first instance
    user = User.query.filter_by(username=username).first()

    #if user already in db, flash and redirect to /login
    if user:
        flash("An account with this username already exists.")
    else:
        #otherwise create new instance of new user
        new_user = User(fname=first_name, lname=last_name, \
                            username=username, password=password)
        db.session.add(new_user)
        db.session.commit()
        flash("{} now registered. Please log in!".format(username))
    return redirect("/login") 


@app.route("/login")
def prompt_login():
    """Prompt user to login"""

    return render_template("login.html")


@app.route("/login", methods=["POST"])
def validate_login():
    """validate username and password"""

    username = request.form.get("Username")
    password = request.form.get("Password")

    user = User.query.filter_by(username=username).first()

    if user:
        if password == user.password:
            session['user'] = user.user_id
            session['fname'] = user.fname 
            flash("You are logged in.")
            return redirect("/user_account")
        else:
            flash("Invalid password. Please try again.")
            return redirect("/login")

    else:
        flash("Username not found. Please try again.")
        return redirect("/home")    



@app.route("/user_account", methods=["GET"])    
def display_data():
    """Display poop events on user page"""

    if session.get('user'):
        user_id = session.get('user')  # <-- why get same num twice?
        user = User.query.get(user_id) # <-- why get same num twice?
        
        # .all() returns list of objects
        user_events = Event.query.filter_by(user_id=user_id).all()
        
        #formatting on frontend
        #loop through list of objects and
        #access event_at on each object and
        #format datetime object (event_at)
        for i in user_events:
            i.event_at = i.event_at.strftime('%B %d, %Y')
            print i.event_at


        return render_template("user_account.html", 
                                user_events=user_events)
    else:
        flash("Not logged in.")
        return redirect("/home")
    


@app.route("/user_account", methods=["POST"])
def submit_data():
    """User adds new poop event"""

    #change naive datetime to be timezone aware

    # .now() not timezone aware
    dt_pac = datetime.datetime.now()

    # instantiate a timezone var
    pac_tz = pytz.timezone('US/Pacific')

    # run .localize() to make timezone aware
    dt_pac = pac_tz.localize(dt_pac).date()
    
    user_id = session.get("user")
    poop_type = request.form.get("type")
    comment = request.form.get("comment")
    print 'user_id', user_id
    print 'poop_type', poop_type
    print 'comment', comment
    new_event = Event(user_id=user_id, comment=comment, 
                        event_at=dt_pac,   #replaced datetime.date.today()
                            type_id=int(poop_type))
    
    db.session.add(new_event)
    db.session.commit()

    
    return redirect("/user_account")

@app.route("/data")
def get_user_data():
    """Get data from"""

    # Take in an ID
    # Look up the details in a database,
    # and return JSON of that.

    if session.get('user'):
        user_id = session.get('user')  # <-- why get same num twice?
        user = User.query.get(user_id) # <-- why get same num twice?
       

    # user_events stores a list of objects
    user_events = Event.query.filter_by(user_id=user_id).all()

    d = {}
    dlist = []
    
    user_data = {}

    for i in user_events:
        #print i.event_type.type_name
        #store every type_name as key with empty list
        user_data[i.event_type.type_name] = []

    
    for i in user_data:
        #this will return list of dict where key = "type" val = "Type 1"
        d["type"] = i
        d["date"] = user_data[i]
        dlist.append(d)

    print dlist    


    
    for i in user_events:
    	#convert Datetime obj to string
        i.event_at = i.event_at.strftime('%B %d, %Y')
        #append event_at to key(type_name)
        user_data[i.event_type.type_name].append(i.event_at)
        # dlist.append(user_data)

    

         

    print ">>> Inside /data route <<<"
    print user_data
    print type(user_data)
    
        
        
    return jsonify(dlist)
    


@app.route("/logout")
def logout():
    """Log out user, remove from session"""

    #if a user is stored in the session
    if session.get('user'):
        del session['user']
        flash("You have been logged out. Have a wonderful day!")
        return redirect("/home")
    else:
        flash("You are logged out.")
        return redirect("/home")

@app.route("/chart")
def chart():
    """Display poop data"""
    

    return render_template("chart.html")                             




if __name__ == "__main__":
    # debug=True once DebugToolbarExtension is invoked

    app.debug = True
    
    connect_to_db(app)

    DebugToolbarExtension(app)
    
    app.run(port=5000, host="0.0.0.0")
