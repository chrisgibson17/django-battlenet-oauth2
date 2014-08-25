try:
    from django.conf import settings
except ImportError:
    pass

from battlenet import constants
from battlenet.community.community import Community

import requests
import warnings

class Character(Community):

    ENDPOINT = '/wow/character/%s/%s'

    def __init__(self, *args, **kwargs):
        super(Character, self).__init__(*args, **kwargs)
        self.name = kwargs.get('name', None)
        self.realm = kwargs.get('realm', None)
        if kwargs.get('fields'):
            if not isinstance(kwargs['fields'], list):
                raise ValueError('fields argument must be a list. E.g. ["achievements", "appearance"].')
            self.fields = kwargs['fields']
        else:
            self.fields = []

    def get(self, name=None, realm=None, fields=[]):
        if name:
            self.name = name
        else:
            if not self.name:
                raise ValueError('Character name required.')

        if realm:
            self.realm = realm
        else:
            if not self.realm:
                raise ValueError('Character realm required.')

        if len(fields) > 0:
            if not isinstance(fields, list):
                raise ValueError('fields argument must be a list. E.g. ["achievements", "appearance"].')
            self.fields = fields

        params = {
            'locale': self.locale,
            'apikey': self.apikey
        }

        if len(self.fields) > 0:
            params['fields'] = ','.join(self.fields)

        response = self._make_request(self.ENDPOINT % (self.realm, self.name), params)

        return response

