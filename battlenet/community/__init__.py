try:
    from django.conf import settings
except ImportError:
    pass
from battlenet import constants

import requests
import warnings

class Community(object):

    def __init__(self, *args, **kwargs):

        if kwargs.get('apikey'):
            self.apikey = kwargs['apikey']
        elif settings:
            try:
                self.apikey = settings.BNET_KEY
            except (AttributeError, ImportError):
                raise ImproperlyConfigured('BattleNet Client Key (BNET_KEY) not found.  Add it to settings.py or pass it to the constructor. E.g bnet = Character(apikey=MY_KEY)')

        if kwargs.get('locale'):
            if kwargs['locale'].split('-')[0] not in constants.LOCALES:
                warnings.warn('Invalid locale provied.  Falling back to \'en\'.  Supported language codes are %s' % (', '.join(constants.LOCALES)))
                self.locale = 'en'
            else:
                self.locale = kwargs['locale']
        else:
            self.locale = 'en'

        if kwargs.get('region'):
            if region not in constants.AVAILABLE_REGIONS:
                raise ValueError("Invalid Region provided.  Region must be one of 'us', 'eu', 'kr' or 'tw'.")
            else:
                self.region = kwargs['region']
        else:
            self.region = 'eu'

        self.params = {
            'locale': self.locale,
            'apikey': self.apikey
        }

    def add_params(self, params):
        for key, value in params.iteritems():
            self.params[key] = value

    def make_request(self, endpoint):

        response = requests.get(constants.BASE_ENDPOINT_URL % self.region + endpoint, params=self.params)

        return response.status_code, response.json()

    def get(self):
        raise NotImplementedError()