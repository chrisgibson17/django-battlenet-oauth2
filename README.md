/django-battlenet-oauth2
=======================

Library for interaction with Battle.net OAuth2 and Community APIs

THIS LIBRARY IS NOT ASSOCIATED WITH, OR ENDORSED BY, BLIZZARD IN ANY WAY.

#Installation

    pip install django-battlenet

# OAuth2

* I use http://requests-oauthlib.readthedocs.org/en/latest/oauth2_workflow.html for OAuth2 interaction.  Install by: pip install requests requests_oauthlib
    - I'm going to look into having this auto install when you run setup.py but havn't done it yet

## Default Values

Default values are:
* key           = settings.BNET_KEY
* secret        = settings.BNET_SECRET
* redirect_uri  = settings.BNET_REDIRECT_URI
* scope         = 'wow.profile'
* region        = 'eu'
* access_token  = None

If you haven't set key/secret/redirect_uri, it will throw an Exception when you initialize
the class, unless you override the default, see below.

_N.B. settings.BNET_KEY and settings.BNET_SECRET should be loaded from environment variables_

Override default values like so:

```python

BattleNet(
    key='Your key',
    secret='Your secret',
    region='us',
    scope='sc2.profile',
    redirect_uri='Your redirect uri',
    access_token='An access token if you have one'
)

```

## Examples:

#### Get Redirect URL & redirect to it

```python

from django.http import HttpResponseRedirect

from battlenet.oauth2 import BattlNetOAuth2

def redirect_to_bnet(request):

    bnet = BattleNetOAuth2()
    url, state = bnet.get_authorization_url()
    # save state somewhere for checking the redirect response against
    request.session['state'] = state
    return HttpResponseRedirect(url)

```

#### Get access token using access code

```python

from battlenet.oauth2 import BattlNetOAuth2

def get_access_token(request):

    if request.GET.get('code'):
        if request.GET.get('state') and request.session.get('state'):
            if request.GET['state'] == request.session['state']:
                bnet = BattleNetOAuth2()
                data = bnet.retrieve_access_token(request.GET['code'])


```

#### Request Battle.net Profile

```python

from battlenet.oauth2 import BattlNetOAuth2

def get_bnet_profile(request):

    bnet = BattleNetOAuth2(scope='sc2.profile', access_token='access_token goes here')
    profile = bnet.get_profile(access_token='or here if you want to make multiple' +
        'requests with same BNet object')

```

#### Request Battletag

```python

from battlenet.oauth2 import BattlNetOAuth2

def get_battletag(request):

    bnet = BattleNetOAuth2(access_token='access_token goes here')
    btag = bnet.get_battletag(access_token='or here')

```

#### Request Account ID

```python

from battlenet.oauth2 import BattlNetOAuth2

def get_accountid(request):

    bnet = BattleNetOAuth2(access_token='access_token goes here')
    account = bnet.get_account_id(access_token='or here')

```

# Community APIs

_Only the WoW APIs are added for now_

### All API requests return a status code and the json response

## Default Values

Default values are:
* apikey        = settings.BNET_KEY
* locale        = 'en'
* region        = 'eu'

If you haven't set key, it will throw an Exception when you initialize the class,
unless you override the default, see below.

_N.B. settings.BNET_KEY should be loaded from environment variable_

Override default values like so:

```python

Achievement(
    apikey='Your key',
    region='us',
    locale='ru_RU'
)

```

## Examples

#### Achievements

```python

from battlenet.community.wow.achievements import Achievement

def get_achievement(request):

    achi = Achievement(achievement='2144')
    status_code, data = achi.get()


```

#### Auctions

```python

from battlenet.community.wow.auctions import Auctions

def get_auctions(request):

    auctions = Auctions(realm='Bloodfeather')
    status_code, data = auctions.get()


```

#### Battle Pets

```python

from battlenet.community.wow.battlepets import BattlePets

def get_battlepet_ability(request):

    ability = BattlePets(id=640, dataset='ability')
    status_code, data = ability.get()


def get_battlepet_species(request):

    species = BattlePets(id='258', dataset='species')
    status_code, data = species.get()


def get_battlepet_stats(request):

    stats = BattlePets(id=258, dataset='stats')
    # level, breed & quality all optional
    status_code, data = stats.get(level=25, breed_id=5, quality_id=4)

```

#### Challenge Modes

```python

from battlenet.community.wow.challengemodes import ChallengeMode

def get_cm_realm_leaderboard(request):

    cms = ChallengeMode(realm='Bloodfeather')
    status_code, data = cms.get()


def get_cm_region_leaderboard(request):

    cms = ChallengeMode()  # defaults to eu
    status_code, data = cms.get()

```

#### Characters

```python

from battlenet.community.wow.characters import Character

def get_character(request):
    # Fields is optional & you can have as many/few as you want
    # This is all of them
    # See Character section of docs: https://dev.battle.net/io-docs
    char = Character(
        name='Shadpanda',
        realm='Bloodfeather',
        fields=[
            'achievements',
            'appearance',
            'feed',
            'guild',
            'hunterPets',
            'items',
            'mounts',
            'pets',
            'petSlots',
            'progression',
            'pvp',
            'quests',
            'reputation',
            'stats',
            'talents',
            'titles',
            'audit'
        ]
    )
    status_code, data = char.get()

```

#### Data APIs

```python

from battlenet.community.wow.data import (
    BattleGroups,
    CharacterRaces,
    CharacterClasses,
    CharacterAchievements,
    GuildAchievements,
    GuildRewards,
    GuildPerks,
    ItemClasses,
    Talents,
    PetTypes,
)

    # all data APIs are the same as this
    status_code, data = BattleGroups().get()

```

#### Guilds

```python

from battlenet.community.wow.guilds import Guild

def get_guild(request):

    # Fields is optional & you can have as many/few as you want
    # This is all of them
    # See Guild section of docs: https://dev.battle.net/io-docs

    guild = Guild(
        name='Lotus',
        realm='Bloodfeather',
        fields=[
            'achievements',
            'members,
            'news',
            'challenge'
        ]
    )
    status_code, data = guild.get()

```

#### Items & Item Sets

```python

from battlenet.community.wow.items import Item, ItemSet

def get_item(request):
    item = Item(id=18803)
    status_code, data = item.get()

def get_itemset(request):
    itemset = ItemSet(id=1060)
    status_code, data = itemset.get()

```

#### PvP

```python

from battlenet.community.wow.pvp import PvP

def get_leaderboard(request):

    # Bracket options are '2v2', '3v3', '5v5' or 'rbg'

    leaderboard = PvP(bracket='2v2')
    status_code, data = leaderboard.get()

```

#### Quests

```python

from battlenet.community.wow.quests import Quest

def get_quest(request):

    quest = Quest(quest=13146)
    status_code, data = quest.get()

```

#### Realm status

```python

from battlenet.community.wow.realms import Realm

def get_realm_status(request):

    # List of realms is optional.  Don't use if you want all realms

    realms = Realm(realms=['Bloodfeather', 'Shadowsong', 'Draenor'])
    status_code, data = realms.get()

```

#### Recipes

```python

from battlenet.community.wow.recipes import Recipe

def get_recipe(request):

    recipe = Recipe(recipe=33994)
    status_code, data = recipe.get()

```

#### Spells

```python

from battlenet.community.wow.spells import Spell

def get_spell(request):

    spell = Spell(recipe=8056)
    status_code, data = spell.get()

```
