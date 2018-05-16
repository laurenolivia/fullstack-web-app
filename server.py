from jinja2 import StrictUndefined
from flask import Flask, render_template, redirect, request, session, flash
from flask_debugtoolbar import DebugToolbarExtension
from model import User, Type, Event, connect_to_db, db 
import datetime

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

    if session.get('user'):
        user_id = session.get('user')
        user = User.query.get(user_id)
        user_events = Event.query.filter_by(user_id=user_id).all()
        return render_template("user_account.html", 
                                user_events=user_events)
    else:
        flash("Not logged in.")
        return redirect("/home")
    


@app.route("/user_account", methods=["POST"])
def submit_data():
    """Display user page"""

    poop_type = request.form.get("type")
    print poop_type
    comment = request.form.get("comment")
    new_event = Event(comment=comment, event_at=datetime.datetime.now(),
                        type_id=int(poop_type))
    
    db.session.add(new_event)
    db.session.commit()

    return redirect("/user_account")



@app.route("/logout")
def logout():
    """Log out user, remove from session"""

    if session.get('user'):
        del session['user']
        flash("You have been logged out. Have a wonderful day!")
        return redirect("/home")
    else:
        flash("You are logged out.")
        return redirect("/home")                    




if __name__ == "__main__":
    # debug=True once DebugToolbarExtension is invoked

    app.debug = True
    
    connect_to_db(app)

    DebugToolbarExtension(app)
    
    app.run(port=5000, host="0.0.0.0")


