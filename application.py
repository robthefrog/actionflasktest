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

app = Flask(__name__)

db_controller = DB_Controller()

@app.route("/")
def users_index():
    context = {'users':db_controller.users}
    return render_template("users.html", **context)

app.run(host='0.0.0.0')