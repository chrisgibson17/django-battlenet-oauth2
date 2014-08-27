from battlenet.community import Community

class PvP(Community):

    ENDPOINT = '/wow/leaderboard/%s'
    _bracket_options = [
        '2v2',
        '3v3',
        '5v5',
        'rbg'
    ]

    def __init__(self, *args, **kwargs):
        super(PvP, self).__init__(*args, **kwargs)
        if kwargs.get('bracket'):
            if kwargs['bracket'] not in self._bracket_options:
                raise ValueError('Invalid bracket provided. Options are %s' % ', '.join(self._bracket_options))
            self.bracket = kwargs.get('bracket')

    def get(self, bracket=None):
        if bracket:
            if bracket not in self._bracket_options:
                raise ValueError('Invalid bracket provided. Options are %s.' % ', '.join(self._bracket_options))
            self.bracket = bracket
        else:
            if not self.bracket:
                raise ValueError('PvP bracket required.')

        return self.make_request(self.ENDPOINT % self.bracket)