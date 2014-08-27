from battlenet.community import Community

class Achievement(Community):

    ENDPOINT = '/wow/achievement/%s'

    def __init__(self, *args, **kwargs):
        super(Achievement, self).__init__(*args, **kwargs)
        self.achievement = kwargs.get('achievement', None)

    def get(self, achievement=None):
        if achievement:
            self.achievement = achievement
        else:
            if not self.achievement:
                raise ValueError('Achievement ID required.')

        return self.make_request(self.ENDPOINT % self.achievement)