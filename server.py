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

    return render_template('homepage.html')

#allow user to register info in db
@app.route('/register')
def register_form():
    """requests username, password"""

    return render_template('register.html')

@app.route("/validate_registration", method="POST")
def validate_registration():
    """Add new user to db"""
    first = request.form.get("First")
    last = request.form.get("Last")
    username = request.form.get("Username")
    password = request.form.get("Password")

    
    
    return render_template("login.html")    

@app.route("/login")
def prompt_login():
    """Prompt user to login"""

    return render_template("login.html")


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


