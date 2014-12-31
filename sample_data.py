from user import User

class Sample_Data:
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

    def __init__(self):
        self.users = [self.user1, self.user2]

    def get_sample_users(self):
        return self.users