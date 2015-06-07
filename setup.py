from distutils.core import setup
from pip.req import parse_requirements
import os


# dirname = os.path.dirname(os.path.realpath(__file__))
# print dirname
# install_reqs = parse_requirements(dirname+'/requirements.txt')
# reqs = [str(ir.req) for ir in install_reqs]
setup(name='battlenet',
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
        'battlenet.community.d3.artisan',
        'battlenet.community.d3.career',
        'battlenet.community.d3.follower',
        'battlenet.community.d3.hero',
        'battlenet.community.d3.item',
    ],
    packages=[
        'battlenet',
        'battlenet.oauth2',
        'battlenet.community'
    ]

)