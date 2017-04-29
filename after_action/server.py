from flask import Flask, render_template, session, jsonify
from flask_orator import Orator

from .models import User, Report
from .blueprints import auth_blueprint

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

app.register_blueprint(auth_blueprint)
app.secret_key = "5s_2fAoaUWyXvSBXPcfM_6NPrSLCvD0ev0y4offiZ3mFLvxfzD_Sjp2pYtcVHJbfkoJDzM5OhLX3ziaFmwXA5coa"

def current_user():
    if 'user' in session:
        return User.where("email", session["user"]).first()
    return False

def is_admin():
    user = current_user()
    return user and user.admin

app.jinja_env.globals.update(current_user=current_user, is_admin=is_admin)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/admin")
def admin():
    return render_template("admin.html", users=User.all(), reports=Report.all())

@app.route("/session")
def show_session():
    print(session)
    return jsonify(session['user'])
