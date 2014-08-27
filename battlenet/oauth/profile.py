from battlenet.oauth import OAuth

class Profile(OAuth):
    ENDPOINT = {
        'wow.profile':'/wow/user/characters',
        'sc2.profile': 'sc2/profile/user'
    }

    def get(self):

        if not self.access_token:
            raise ValueError('No access token available.')

        return self.make_request(self.ENDPOINT[self.scope])