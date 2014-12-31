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

application = Flask(__name__)

assets = Environment(application)
assets.url = application.static_url_path
scss = Bundle('all.scss', filters='scss', output='all.css')
assets.register('scss_all', scss)

db_controller = DB_Controller()

@application.route("/")
def users_index():
    context = {'users':db_controller.users}
    return render_template("users.html", **context)

if __name__ == '__main__':
    application.run(host='0.0.0.0')
