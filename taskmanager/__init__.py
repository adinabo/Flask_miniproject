import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
if os.path.exists("env.py"):
    import env

app = Flask(__name__) # create an instance an store it in app that take default name module
# two app configuration variables:
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_URL")

# create instance of the SQLALCHEMY class and assign to var db and set to our Flask app
db = SQLAlchemy(app)

from taskmanager import routes

