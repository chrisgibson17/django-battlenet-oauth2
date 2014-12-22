try:
    from django.conf import settings
except ImportError:
    pass

import urllib
try:
    from requests_oauthlib import OAuth2Session
except ImportError:
    raise ImportError(
        'Requests_oauthlib package not installed.  (sudo) pip install requests requests_oauthlib')

from battlenet import constants


class BattleNetOAuth2(object):

    def __init__(self, key=None, secret=None, region='eu', scope='wow.profile', redirect_uri=None, access_token=None):

        if key:
            self.BNET_KEY = key
        else:
            try:
                self.BNET_KEY = settings.BNET_KEY
            except (AttributeError, ImportError):
                raise ValueError(
                    'BattleNet Client Key (BNET_KEY) not found.  Add it to settings or pass it to the BattleNet constructor. E.g BattleNet(key=MY_KEY)')

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
            raise ValueError(
                "Invalid Region provided.  Region must be one of 'us', 'eu', 'kr', or 'tw'.")

        if scope in constants.AVAILABLE_SCOPES:
            self.scope = scope
        else:
            raise ValueError(
                "Invalid scope provided.  Region must be one of 'wow.profile' or 'sc2.profile'.")

        self.access_token = access_token

    def get_authorization_url(self):

        if not self.BNET_REDIRECT_URI:
            raise ValueError(
                'BattleNet Redirect URi (BNET_REDIRECT_URI) not found.  Add it to settings or pass it to the BattleNet constructor. E.g BattleNet(redirect_uri=REDIRECT_URI)')

        self.oauth = OAuth2Session(
            self.BNET_KEY, redirect_uri=self.BNET_REDIRECT_URI, scope=[self.scope])
        auth_url, state = self.oauth.authorization_url(
            constants.BNET_AUTH_URL % self.region)
        return auth_url, state

    def retrieve_access_token(self, access_code):

        if not access_code:
            raise ValueError('No access_code provided.')

        if not self.BNET_SECRET:
            raise ValueError(
                'BattleNet Clienut Secret (BNET_SECRET) not found in settings.  Add it to settings or pass it to the BattleNet constructor. E.g OAuth(secret=MY_SECRET)')

        if not self.BNET_REDIRECT_URI:
            raise ValueError(
                'BattleNet Redirect URi (BNET_REDIRECT_URI) not found.  Add it to settings or pass it to the BattleNet constructor. E.g OAuth(redirect_uri=REDIRECT_URI)')

        self.oauth = OAuth2Session(
            self.BNET_KEY, redirect_uri=self.BNET_REDIRECT_URI, scope=[self.scope])

        token_data = self.oauth.fetch_token(
            constants.BNET_TOKEN_URL % self.region,
            code=access_code,
            client_secret=self.BNET_SECRET
        )

        self.access_token = token_data['access_token']
        return token_data

    def _set_token(self, token):
        self.access_token = token
        if not self.oauth:
            self.oauth = OAuth2Session(
                self.BNET_KEY, redirect_uri=self.BNET_REDIRECT_URI, token=token)
        else:
            self.oauth.token = token

    def _make_request(self, endpoint):
        if not self.access_token:
            raise ValueError('No access token available.')

        if not self.oauth:
            self.oauth = OAuth2Session(
                self.BNET_KEY, redirect_uri=self.BNET_REDIRECT_URI)

        r = self.oauth.get(constants.BASE_ENDPOINT_URL %
                           self.region + endpoint)

        return r.status_code, r.json()

    def get_battletag(self, access_token=None):
        if access_token:
            self._set_token(access_token)

        return self._make_request('/account/user/battletag')

    def get_profile(self, access_token=None):
        if access_token:
            self._set_token(access_token)

        if self.scope == 'wow.profile':
            return self._make_request('/wow/user/characters')

        if self.scope == 'sc2.profile':
            return self._make_request('/sc2/profile/user')

    def get_account_id(self, access_token=None):

        if access_token:
            self._set_token(access_token)

        return self._make_request('/account/user/id')
