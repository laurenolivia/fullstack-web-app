from jinja2 import StrictUndefined
from flask import Flask, render_template, redirect, request, session
from flask_debugtoolbar import DebugToolbarExtension
from model import connect_to_db, db 

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

@app.route("/validate_registration", methods="POST")
def validate_registration():
    """Validate user and new user to db"""

    first_name = request.form.get("First")
    last_name = request.form.get("Last")
    username = request.form.get("Username")
    password = request.form.get("Password")

    #query for username in db, return first instance
    user = User.query.get(username=username).first()

    #if user already in db, flash and redirect to /login
    if user:
        flash("An account with this username already exists.")
        return redirect('/login')
    else:
        #otherwise create new instance of new user
        new_user = User(fname=first_name, lname=last_name, \
                            username=username, password=password)
        db.session.add(new_user)
        db.session.commit()
        flash("You are now registered. Please log in!")
        return redirect("/login")
   
    return render_template("login.html")    


@app.route("/login")
def prompt_login():
    """Prompt user to login"""


    return render_template("login.html")

@app.route("/validate_login", methods="POST")
def validate_login():
    """validate username password"""

    username = request.form.get("Username")
    password = request.form.get("Password")

    user = User.query.get(username=username).first()

    if user:
        if password == user.password:
            session['user'] = user.user_id
            flash("You are logged in.")
            redirect("/user_account")
        else:
            flash("Invalid password. Please try again.")
            redirect("/login")

    else:
        flash("Username does not exist.")
        redirect("/home")            


@app.route("/user_account")
def display_account():
    """Display user page"""

    return render_template("user_account.html")



if __name__ == "__main__":
    # debug=True once DebugToolbarExtension is invoked

    app.debug = True
    
    connect_to_db(app)

    DebugToolbarExtension(app)
    
    app.run(port=5000, host="0.0.0.0")


