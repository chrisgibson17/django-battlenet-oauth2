AVAILABLE_REGIONS = [
    'us',
    'eu',
    'kr',
    'tw'
]

AVAILABLE_SCOPES = [
    'wow.profile',
    'sc2.profile'
]

LOCALES = [
    'en',
    'es',
    'pt',
    'it',
    'de',
    'fr',
    'pl',
    'ru',
    'tr',
    'ko',
    'zh'
]

BNET_AUTH_URI = 'https://%s.battle.net/oauth/authorize'
BNET_TOKEN_URI = 'https://%s.battle.net/oauth/token'

BASE_ENDPOINT_URL = 'https://%s.api.battle.net'

# ENDPOINTS = {
#     'oauth': {
#         'wow.profile': {
#             'url': BASE_ENDPOINT_URL + '/wow/user/characters',
#         },
#         'sc2.profile': {
#             'url': BASE_ENDPOINT_URL + '/sc2/profile/user'
#         },
#         'account': {
#             'battletag': {
#                 'url': BASE_ENDPOINT_URL + '/account/user/battletag'
#             },
#             'accountid': {
#                 'url': BASE_ENDPOINT_URL + '/account/user/id'
#             }
#         },
#     },
#     'api': {
#         'wow': {
#             'achievement': {
#                 'url': BASE_ENDPOINT_URL + '/wow/achievement/%s',
#                 'required_params': {
#                     'apikey': '%s'
#                 },
#                 'optional_params': {
#                     'locale': 'en'
#                 }
#             },
#             'auctions': {
#                 'url': BASE_ENDPOINT_URL + '/wow/auction/data/%s',
#                 'required_params': {
#                     'apikey': '%s'
#                 },
#                 'optional_params': {
#                     'locale': 'en'
#                 }
#             },
#             'battlepet': {
#                 'url': BASE_ENDPOINT_URL + '/wow/battlePet/%s/%s',
#                 'required_fields': {
#                     'info_type': '%s', # abilities / species / stats
#                     'info_type_id': '%s' # abilityid / speciesid /speciesid
#                 }
#                 'required_params': {
#                     'apikey': '%s'
#                 },
#                 'optional_parmas': {
#                     'locale': 'en',
#                     'level': '%s',
#                     'breedId': '%s',
#                     'qualityId': '%s'
#                 }
#             },
#             'challengemodes': {
#                 'url': BASE_ENDPOINT_URL + '/wow/challenge/%s',
#                 'required_fields': {
#                     'realm_or_region': '%s' # realm name or 'region'
#                 },
#                 'required_params': {
#                     'apikey': '%s'
#                 },
#                 'optional_params': {
#                     'locale': 'en'
#                 }
#             }

#         },
#         'sc2': {

#         },
#         'd3': {

#         }
#     }
# }