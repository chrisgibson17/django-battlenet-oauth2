from django.conf import settings
from django.http import HttpResponseRedirect
from django.core.exceptions import ImproperlyConfigured

import urllib
import requests

class BearerAuth(requests.auth.AuthBase):
    def __init__(self, access_token):
        self.access_token = access_token

    def __call__(self, r):
        r.headers['Authorization'] = 'Bearer %s' % self.access_token
        return r

AVAILABLE_REGIONS = [
    'us',
    'eu',
    'kr',
    'tw',
    'cn'
]

AVAILABLE_SCOPES = [
    'wow.profile',
    'sc2.profile'
]

class BattleNet(object):

    def __init__(self, key=None, secret=None, region='eu', scope='wow.profile', redirect_uri=None, access_token=None):
        if key:
            self.BNET_KEY = key
        else:
            try:
                self.BNET_KEY = settings.BNET_KEY
            except AttributeError:
                raise ImproperlyConfigured('BattleNet Client Key (BNET_KEY) not found in settings.  Add it to settings or pass it to the BattleNet constructor. E.g bnet = BattlNet(key=MY_KEY)')

        if secret:
            self.BNET_SECRET = secret
        else:
            try:
                self.BNET_SECRET = settings.BNET_SECRET
            except AttributeError:
                raise ImproperlyConfigured('BattleNet Client Secret (BNET_SECRET) not found in settings.  Add it to settings or pass it to the BattleNet constructor. E.g bnet = BattlNet(secret=MY_SECRET)')

        if redirect_uri:
            self.BNET_REDIRECT_URI = redirect_uri
        else:
            try:
                self.BNET_REDIRECT_URI = settings.BNET_REDIRECT_URI
            except AttributeError:
                raise ImproperlyConfigured('BattleNet Redirect URi (BNET_REDIRECT_URI) not found in settings.  Add it to settings or pass it to the BattleNet constructor. E.g bnet = BattlNet(redirect_uri=REDIRECT_URI)')

        if region in AVAILABLE_REGIONS:
            self.region = region
        else:
            raise ValueError("Invalid Region provided.  Region must be one of 'us', 'eu', 'kr', 'tw' or 'cn'.")

        if scope in AVAILABLE_SCOPES:
            self.scope = scope
        else:
            raise ValueError("Invalid scope provided.  Region must be one of 'wow.profile' or 'sc2.profile'.")

        self.BNET_AUTH_URI = 'https://%s.battle.net/oauth/authorize'
        self.BNET_TOKEN_URI = 'https://%s.battle.net/oauth/token'

        self._endpoints = {
            'wow.profile': 'https://%s.api.battle.net/wow/user/characters',
            'sc2.profile': 'https://%s.api.battle.net/sc2/profile/user'
        }

        self.access_token = access_token

    def has_access_token(self):
        if self.access_token is None:
            return False
        return True

    def redirect_to_authorization(self, state=None):

        if not state:
            raise ValueError('No state passed.')

        params = {
            'client_id': self.BNET_KEY,
            'redirect_uri': self.BNET_REDIRECT_URI,
            'response_type': 'code',
            'scope': self.scope,
            'state': state
        }

        query = urllib.urlencode(params)

        return HttpResponseRedirect(self.BNET_AUTH_URI % self.region + "?" + query)

    def retrieve_access_token(self, access_code=None):

        if not access_code:
            raise ValueError('No access_code provided.')

        params = {
            'scope': self.scope,
            'redirect_uri': self.BNET_REDIRECT_URI,
            'code': access_code,
            'grant_type': 'authorization_code'
        }

        r = requests.post(
            self.BNET_TOKEN_URI % self.region,
            data=params,
            auth=requests.auth.HTTPBasicAuth(self.BNET_KEY, self.BNET_SECRET)
        )

        r.raise_for_status()

        data = r.json()

        self.access_token = data['access_token']
        self.account_id = data['accountId']

        return data

    def get_battlenet_profile(self):

        if not self.access_token:
            raise ValueError('No access token available.')

        r = requests.post(
            self._endpoints[self.scope] % self.region,
            auth=BearerAuth(self.access_token)
        )

        r.raise_for_status()

        data = r.json()

        return data

    def get_battletag(self):
        if not self.access_token:
            raise ValueError('No access token available.')

        r = requests.get(
            'https://eu.api.battle.net/account/user/battletag',
            auth=BearerAuth(self.access_token)
        )

        r.raise_for_status()

        data = r.json()

        return data

    def get_userid(self):
        if not self.access_token:
            raise ValueError('No access token available.')

        r = requests.get(
            'https://eu.api.battle.net/account/user/id',
            auth=BearerAuth(self.access_token)
        )

        r.raise_for_status()

        data = r.json()

        return data
