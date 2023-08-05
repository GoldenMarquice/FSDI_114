from flask import Flask # from the flask module, import the flask class
from flask import render_template

app = Flask(__name__) # Initialixe the Flask class into app, now an object

@app.get("/")       #Flask decorator that creates routes
def index():
    me = {          # python dictionary (key and value pairs)
        "first_name": "Marquice",
        "last_name": "Bowman",
        "hobbies": "Money",
        "is_active": True
    }
    return me       # with flask, returning a valid dictionary from a 
                    # view function will automatically convert it to 
                    #JSON
@app.get("/about")
def about_me():
    return render_template("about.html")