try:
    from django.conf import settings
except ImportError:
    pass

import urllib
try:
    import requests
except ImportError:
    raise ImportError('Requests package not installed.  (sudo) pip install requests==2.*')

from battlenet.oauth.oauth import OAuth

class BattleTag(OAuth):

    ENDPOINT = '/account/user/battletag'

    def get(self):

        if not self.access_token:
            raise ValueError('No access token available.')

        response = self._make_request(self.ENDPOINT)

        return response