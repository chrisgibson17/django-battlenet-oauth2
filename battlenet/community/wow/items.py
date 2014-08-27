from battlenet.community import Community

class Item(Community):

    ENDPOINT = '/wow/item/%s'
    error_text = 'Item ID required.'

    def __init__(self, *args, **kwargs):
        super(Item, self).__init__(*args, **kwargs)
        self.id = kwargs.get('id')

    def get(self, id=None):
        if id:
            self.id = id
        else:
            if not self.id:
                raise ValueError(error_text)

        return self.make_request(self.ENDPOINT % self.id)

class ItemSet(Item):
    ENDPOINT = '/wow/item/set/%s'
    error_text = 'Set ID required.'