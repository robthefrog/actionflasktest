from user import User
from action_item import Action_Item
import json

class DB_Controller:
    users = []
    context1 = {
        'id': 1,
        'first_name': 'Robert',
        'last_name': 'Goddard',
        'email': 'robthefrog@gmail.com'
    }
    user1 = User(**context1)
    context2 = {
        'id': 2,
        'first_name': 'Terry',
        'last_name': 'Goddard',
        'email': 'terry.goddard@gmail.com'
    }
    user2 = User(**context2)

    def get_users_json(self):
        users_json_list = []
        for user in self.users:
            users_json_list.append(user.to_json())
        return json.dumps(users_json_list)

    def valid_api_key(self, api_key):
        for user in self.users:
            if user.api_key == api_key:
                return True

        return False

    def __init__(self):
        self.users = [self.user1, self.user2]