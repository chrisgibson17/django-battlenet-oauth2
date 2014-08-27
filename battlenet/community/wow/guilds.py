from battlenet.community import Community


class Guild(Community):

    ENDPOINT = '/wow/guild/%s/%s'
    # Unused atm
    _available_fields = [
        'news',
        'achievements',
        'challenge',
        'members'
    ]

    def __init__(self, *args, **kwargs):
        super(Guild, self).__init__(*args, **kwargs)

        self.name = kwargs.get('name', None)
        self.realm = kwargs.get('realm', None)

        if kwargs.get('fields'):
            if not isinstance(kwargs['fields'], list):
                raise ValueError(
                    'fields argument must be a list. E.g. ["achievements", "news"].'
                )
            self.fields = kwargs['fields']
        else:
            self.fields = []

    def get(self, name=None, realm=None, fields=[]):
        if name:
            self.name = name
        else:
            if not self.name:
                raise ValueError('Guild name required.')

        if realm:
            self.realm = realm
        else:
            if not self.realm:
                raise ValueError('Guild realm required.')

        if len(fields) > 0:
            if not isinstance(fields, list):
                raise ValueError(
                    'fields argument must be a list. E.g. ["achievements", "news"].'
                )
            self.fields = fields

        if len(self.fields) > 0:
            self.add_params(
                {
                    'fields': ','.join(self.fields)
                }
            )

        return self.make_request(self.ENDPOINT % (self.realm, self.name))
