from flask import Blueprint, session, jsonify
import after_action.models as models

auth_blueprint = Blueprint("auth", __name__, url_prefix="/auth")

@auth_blueprint.route("/")
def index():
    if "user" in session:
        current_user = session["user"]
    else:
        current_user = None

    return jsonify(current_user)

# TODO actually do the email-based, passwordless auth
@auth_blueprint.route("/login/<string:email>")
def login_as(email):
    user = models.User.where("email", email).first()
    if user:
        session["user"] = user.email
        return jsonify({"logged_in": True})
    else:
        return jsonify({"logged_in": False})

@auth_blueprint.route("/logout")
def logout():
    del session["user"]
    return jsonify(True)
