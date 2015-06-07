from distutils.core import setup

setup(name='django-battlenet',
    license='MIT',
    version='0.1',
    py_modules=[
        'battlenet.constants',
        'battlenet.oauth2',
        'battlenet.community.wow.achievements',
        'battlenet.community.wow.auctions',
        'battlenet.community.wow.battlepets',
        'battlenet.community.wow.challengemodes',
        'battlenet.community.wow.characters',
        'battlenet.community.wow.guilds',
        'battlenet.community.wow.items',
        'battlenet.community.wow.pvp',
        'battlenet.community.wow.quests',
        'battlenet.community.wow.realms',
        'battlenet.community.wow.recipe',
        'battlenet.community.wow.spells',
        'battlenet.community.wow.data',
        'battlenet.community.sc2',
        'battlenet.community.d3'
    ],
    packages=['battlenet', 'battlenet.oauth2', 'battlenet.community'],
    install_requires=[
        'requests_oauth2'
    ],
    description='API wrapper for Blizzards Community APIs & oAuth login',
    author='Chris Gibson',
    author_email='chris@chrisgibson.io',
    url='https://github.com/chrisgibson17/django-battlenet-oauth2',
    download_url= 'https://github.com/chrisgibson17/django-battlenet-oauth2/archive/master.tar.gz',
)