from user import User
from action_item import Action_Item

class DB_Controller:
    users = []
    context = {
        'id': 1,
        'first_name': 'Robert',
        'last_name': 'Goddard',
        'email': 'robthefrog@gmail.com'
    }
    user1 = User(**context)
    context = {
        'id': 2,
        'first_name': 'Terry',
        'last_name': 'Goddard',
        'email': 'terry.goddard@gmail.com'
    }
    user2 = User(**context)

    def __init__(self):
        self.users = [self.user1, self.user2]