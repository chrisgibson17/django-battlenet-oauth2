try:
    from django.conf import settings
except ImportError:
    pass

import urllib
try:
    import requests
except ImportError:
    raise ImportError('Requests package not installed.  (sudo) pip install requests==2.*')

from battlenet.oauth import OAuth

class AccountID(OAuth):

    ENDPOINT = '/account/user/id'

    def get(self):

        if not self.access_token:
            raise ValueError('No access token available.')

        return self.make_request(self.ENDPOINT)