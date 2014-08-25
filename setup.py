from distutils.core import setup
setup(name='battlenet',
    version='0.1',
    py_modules=[
        'battlenet.constants',
        'battlenet.oauth.headers',
        'battlenet.oauth.oauth',
        'battlenet.oauth.profile',
        'battlenet.oauth.battletag',
        'battlenet.oauth.account',
        'battlenet.community.community',
        'battlenet.community.wow.character'
    ],
)