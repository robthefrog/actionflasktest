from user import User
from action_item import Action_Item

class Sample_Data:
    # Sample users
    context = {
        'id': 1,
        'first_name': 'John',
        'last_name': 'Doe',
        'email': 'John.Doe@email.com'
    }
    user1 = User(**context)
    
    context = {
        'id': 2,
        'first_name': 'Jane',
        'last_name': 'Doe',
        'email': 'Jane.Doe@gmail.com'
    }
    user2 = User(**context)

    # Sample action items
    context = {
        'id': 1,
        'user_id': 1,
        'text': 'Cook the turkey.',
        'due_date': 'Jan 1, 2015',
        'created_date': 'Dec 23, 2015',
        'reattacks': ["I need to buy the turkey first."],
        'complete': False
    }
    action_item1 = Action_Item(**context)

    context = {
        'id': 2,
        'user_id': 1,
        'text': 'Take the dog for a walk.',
        'due_date': 'Dec 30, 2014',
        'created_date': 'Dec 23, 2014',
        'reattacks': [],
        'complete': True
    }
    action_item2 = Action_Item(**context)

    context = {
        'id': 3,
        'user_id': 2,
        'text': 'Finish writing the novel',
        'due_date': 'Jan 1, 2015',
        'created_date': 'Dec 23, 2015',
        'reattacks': ["Typewriter caught on fire.", "I now have a new Typewriter."],
        'complete': False
    }
    action_item3 = Action_Item(**context)

    context = {
        'id': 4,
        'user_id': 2,
        'text': 'Clean the bathroom',
        'due_date': 'Dec 30, 2014',
        'created_date': 'Dec 23, 2014',
        'reattacks': [],
        'complete': True
    }
    action_item4 = Action_Item(**context)

    def __init__(self):
        self.users = [self.user1, self.user2]
        self.action_items = [self.action_item1, self.action_item2, self.action_item3, self.action_item4]

    def get_sample_users(self):
        return self.users

    def get_sample_action_items(self):
        return self.action_items