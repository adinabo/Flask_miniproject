from flask import render_template
from taskmanager import app, db

#create a basic app route using root-level directory of slash
@app.route("/")
def home():
    return render_template("base.html")