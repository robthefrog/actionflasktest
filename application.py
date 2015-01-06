from flask import Flask
from flask import render_template
from db_controller import DB_Controller

application = Flask(__name__)

db_controller = DB_Controller()

@application.route("/")
@application.route("/users")
def users_index():
    context = {'users':db_controller.users}
    return render_template("users.html", **context)

@application.route("/<api_key>/users")
def users_json(api_key):
    if (db_controller.valid_api_key(api_key)):
        return db_controller.get_users_json()
    else:
        return "{\"Error\": \"Invalid API key\"}"

@application.route("/<api_key>/<int:user_id>/action_items")
def action_items_for_user_json(api_key, user_id):
    if (db_controller.valid_api_key(api_key)):
        return db_controller.get_action_items_for_user_json(user_id)
    else:
        return "{\"Error\": \"Invalid API key\"}"

if __name__ == '__main__':
    application.run(host='0.0.0.0')
