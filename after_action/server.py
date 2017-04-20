from flask import Flask, render_template
from flask_orator import Orator

from .models import User, Report

app = Flask("After the Action")
app.config["ORATOR_DATABASES"] = {
    "development": {
        "driver": "pgsql",
        "database": "after_the_action",
        "user": "after_the_action",
        "password": "after_action_test",
    }
}

db = Orator(app)

@app.route("/")
def index():
    return render_template("index.html", users=User.all(), reports=Report.all())
