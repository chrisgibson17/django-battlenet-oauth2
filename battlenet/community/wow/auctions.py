from battlenet.community import Community

class Auctions(Community):

    ENDPOINT = '/wow/auction/data/%s'

    def __init__(self, *args, **kwargs):
        super(Auctions, self).__init__(*args, **kwargs)
        self.realm = kwargs.get('realm', None)

    def get(self, realm=None):
        if realm:
            self.realm = realm
        else:
            if not self.realm:
                raise ValueError('Realm name required.')

        return self.make_request(self.ENDPOINT % self.realm)