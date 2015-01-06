import hashlib
import random

class User:

    id = 0
    api_key = 0
    first_name = 'First Name'
    last_name = 'Last Name'
    email = 'example@nothing.xyz'
    action_items = []

    def __init__(self, **kwargs):
        self.id = kwargs.get('id', 0)
        self.api_key = hashlib.sha256(str(random.getrandbits(256)).encode('utf-8')).hexdigest().upper()
        self.first_name = kwargs.get('first_name', '')
        self.last_name = kwargs.get('last_name', '')
        self.email = kwargs.get('email', '')

    def to_dict(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email
        }