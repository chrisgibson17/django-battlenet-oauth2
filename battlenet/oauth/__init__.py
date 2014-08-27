try:
    from django.conf import settings
except ImportError:
    pass

import urllib
try:
    import requests
except ImportError:
    raise ImportError('Requests package not installed.  (sudo) pip install requests==2.*')

from battlenet import constants

class BearerAuth(requests.auth.AuthBase):
    def __init__(self, access_token):
        self.access_token = access_token

    def __call__(self, r):
        r.headers['Authorization'] = 'Bearer %s' % self.access_token
        return r

class OAuth(object):

    def __init__(self, key=None, secret=None, region='eu', scope='wow.profile', redirect_uri=None, access_token=None):

        if key:
            self.BNET_KEY = key
        else:
            try:
                self.BNET_KEY = settings.BNET_KEY
            except (AttributeError, ImportError):
                raise ValueError('BattleNet Client Key (BNET_KEY) not found.  Add it to settings or pass it to the BattleNet constructor. E.g BattleNet(key=MY_KEY)')

        if secret:
            self.BNET_SECRET = secret
        else:
            try:
                self.BNET_SECRET = settings.BNET_SECRET
            except (AttributeError, ImportError):
                pass

        if redirect_uri:
            self.BNET_REDIRECT_URI = redirect_uri
        else:
            try:
                self.BNET_REDIRECT_URI = settings.BNET_REDIRECT_URI
            except (AttributeError, ImportError):
                pass

        if region in constants.AVAILABLE_REGIONS:
            self.region = region
        else:
            raise ValueError("Invalid Region provided.  Region must be one of 'us', 'eu', 'kr', or 'tw'.")

        if scope in constants.AVAILABLE_SCOPES:
            self.scope = scope
        else:
            raise ValueError("Invalid scope provided.  Region must be one of 'wow.profile' or 'sc2.profile'.")

        self.access_token = access_token

    def get_authorization_url(self, state=None):

        if not state:
            raise ValueError('No state passed.')

        if not self.REDIRECT_URI:
            raise ValueError('BattleNet Redirect URi (BNET_REDIRECT_URI) not found.  Add it to settings or pass it to the BattleNet constructor. E.g BattleNet(redirect_uri=REDIRECT_URI)')

        params = {
            'client_id': self.BNET_KEY,
            'redirect_uri': self.BNET_REDIRECT_URI,
            'response_type': 'code',
            'scope': self.scope,
            'state': state
        }

        query = urllib.urlencode(params)

        return contstants.BNET_AUTH_URI % self.region + "?" + query

    def retrieve_access_token(self, access_code=None):

        if not access_code:
            raise ValueError('No access_code provided.')

        if not self.BNET_SECRET:
            raise ValueError('BattleNet Client Secret (BNET_SECRET) not found in settings.  Add it to settings or pass it to the BattleNet constructor. E.g OAuth(secret=MY_SECRET)')

        if not self.REDIRECT_URI:
            raise ValueError('BattleNet Redirect URi (BNET_REDIRECT_URI) not found.  Add it to settings or pass it to the BattleNet constructor. E.g OAuth(redirect_uri=REDIRECT_URI)')

        params = {
            'scope': self.scope,
            'redirect_uri': self.BNET_REDIRECT_URI,
            'code': access_code,
            'grant_type': 'authorization_code'
        }

        r = requests.post(
            constants.BNET_TOKEN_URI % self.region,
            data=params,
            auth=requests.auth.HTTPBasicAuth(self.BNET_KEY, self.BNET_SECRET)
        )

        r.raise_for_status()

        data = r.json()

        self.access_token = data['access_token']

        return data

    def make_request(self, endpoint):
        r =  requests.post(
            constants.BASE_ENDPOINT_URL % self.region + endpoint,
            auth=BearerAuth(self.access_token)
        )

        return r.status_code, r.json()

    def get(self):
        pass
