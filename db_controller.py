from user import User
from action_item import Action_Item
from sample_data import Sample_Data
import json

class DB_Controller:
    sample_data = Sample_Data()

    def get_users_json(self):
        users_json_list = []
        for user in self.users:
            users_json_list.append(user.to_json())
        return json.dumps(users_json_list)

    def get_action_items_for_user_json(self, user_id):
        action_items_list = []
        for action_item in self.action_items:
            if action_item.user_id == user_id:
                action_items_list.append(action_item.to_json())
        return json.dumps(action_items_list)

    def valid_api_key(self, api_key):
        for user in self.users:
            if user.api_key == api_key:
                return True

        return False

    def __init__(self):
        self.users = self.sample_data.get_sample_users()
        self.action_items = self.sample_data.get_sample_action_items()