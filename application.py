from flask import Flask
from flask import render_template
from flask import redirect
from flask import url_for
from flask import request
from flask import make_response
from flask import flash
from flask.ext.assets import Bundle
from flask.ext.assets import Environment
import json
from db_controller import DB_Controller
from user import User

app = Flask(__name__)

assets = Environment(app)
assets.url = app.static_url_path
scss = Bundle('all.scss', filters='scss', output='all.css')
assets.register('scss_all', scss)

db_controller = DB_Controller()

@app.route("/users")
def users_index():
    context = {'users':db_controller.users}
    return render_template("users.html", **context)

app.run(host='0.0.0.0')
