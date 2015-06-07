from battlenet.community import Community

class Item(Community):

    ENDPOINT = "/d3/data/item/%s"

    def __init__(self, *args, **kwargs):
        super(Item, self).__init__(*args, **kwargs)
        self.item_data = kwargs.get('item_data')

    def get(self, item_data=None):
        if item_data:
            self.item_data = item_data
        if not self.item_data:
            raise ValueError("Item ID required.")

        return self.make_request(self.ENDPOINT % self.item_data)
