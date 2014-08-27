from battlenet.oauth import OAuth

class BattleTag(OAuth):

    ENDPOINT = '/account/user/battletag'

    def get(self):

        if not self.access_token:
            raise ValueError('No access token available.')

        return self.make_request(self.ENDPOINT)