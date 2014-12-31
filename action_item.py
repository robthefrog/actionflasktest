import datetime

class Action_Item:
    id = 0
    user_id = 0
    text = ''
    due_date = ''
    created_date = ''
    reattacks = []
    complete = False

    def __init__(self, **kwargs):
        id = kwargs.get('id', 0)
        user_id = kwargs.get('user_id', 0)
        text = kwargs.get('text', '')
        due_date = kwargs.get('due_date', '')
        created_date = datetime.datetime.now() 