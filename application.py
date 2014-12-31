from flask import Flask
from flask import render_template
from flask import redirect
from flask import url_for
from flask import request
from flask import make_response
from flask import flash
import json
from db_controller import DB_Controller
from user import User

application = Flask(__name__)

db_controller = DB_Controller()

@application.route("/")
def users_index():
    context = {'users':db_controller.users}
    return render_template("users.html", **context)

@application.route("/<api_key>/users")
def users_json(api_key):
    if (db_controller.valid_api_key(api_key)):
        return db_controller.get_users_json()
    else:
        return "{\"Error\": \"Invalid API key\"}"

if __name__ == '__main__':
    application.run(host='0.0.0.0')
