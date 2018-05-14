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
@app.route('/register', method=["GET"])
def register_form():
    """requests username, password"""


    return render_template('homepage.html')





if __name__ == "__main__":
    # debug=True once DebugToolbarExtension is invoked

    app.debug = True
    
    connect_to_db(app)

    DebugToolbarExtension(app)
    
    app.run(port=5000, host="0.0.0.0")


