from battlenet.community import Community

class ChallengeMode(Community):

    ENDPOINT = '/wow/challenge/%s'

    def __init__(self, *args, **kwargs):
        super(ChallengeMode, self).__init__(*args, **kwargs)
        self.request_type = kwargs.get('realm', 'region')

    def get(self, realm=None):
        if realm:
            self.request_type = realm

        # ??? for region
        return self.make_request(self.ENDPOINT % self.request_type)