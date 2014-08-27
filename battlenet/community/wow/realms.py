from battlenet.community import Community

class Realm(Community):

    ENDPOINT = '/wow/realm/status'

    def __init__(self, *args, **kwargs):
        super(Realm, self).__init__(*args, **kwargs)

        if kwargs.get('realms'):
            if not isinstance(kwargs['realms'], list):
                raise ValueError(
                    'realms argument must be a list. E.g. ["achievements", "appearance"].'
                )
            self.realms = kwargs['realms']
        else:
            self.realms = []

    def get(self, realms=[]):

        if len(realms) > 0:
            if not isinstance(realms, list):
                raise ValueError(
                    'realms argument must be a list. E.g. ["achievements", "appearance"].'
                )
            self.realms = realms

        if len(self.realms) > 0:
            self.add_params(
                {
                    'realms': ','.join(self.realms)
                }
            )
        return self.make_request(self.ENDPOINT)