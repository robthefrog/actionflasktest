class Action_Item:
    id = 0
    user_id = 0
    text = ''
    due_date = ''
    created_date = ''
    reattacks = []
    complete = False

    def __init__(self, **kwargs):
        self.id = kwargs.get('id', 0)
        self.user_id = kwargs.get('user_id', 0)
        self.text = kwargs.get('text', '')
        self.due_date = kwargs.get('due_date', '')
        self.created_date = kwargs.get('created_date', '')
        self.reattacks = kwargs.get('reattacks', [])
        self.complete = kwargs.get('complete', False)

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'text': self.text,
            'due_date': self.due_date,
            'created_date': self.created_date,
            'reattacks': self.reattacks,
            'complete': self.complete
        }