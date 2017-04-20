from flask import Flask
from flask_orator import Orator

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
