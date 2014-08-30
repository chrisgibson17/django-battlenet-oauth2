django-battlenet-oauth2
=======================

Basic class for getting Access Token &amp; Account Information from battlenet

THIS LIBRARY IS NOT ASSOCIATED WITH, OR ENDORSED BY, BLIZZARD IN ANY WAY.

#_I need to update this a lot _

##Installation
#####(Only tested on OSX but I assume Windows is the same/simailar)

Clone the repo: git clone git@github.com:chrisgibson17/django-battlenet-oauth2.git (or use GitHub client)

Navigate to the local repo and run: (sudo) python setup.py install

## OAuth2

* I use http://requests-oauthlib.readthedocs.org/en/latest/oauth2_workflow.html for OAuth2 interaction.  Install by: pip install requests requests_oauthlib
    - I'm going to look into having this auto install when you run setup.py but havn't done it yet

## Default Values

Default values are:
* key           = settings.BNET_KEY **
* secret        = settings.BNET_SECRET **
* redirect_uri  = settings.BNET_REDIRECT_URI
* scope         = 'wow.profile'
* region        = 'eu'
* access_token  = None

If you haven't set key/secret/redirect_uri, it will throw an Exception when you initialize
the class, unless you override the default, see below.

_ N.B. settings.BNET_KEY and settings.BNET_SECRET should be loaded from environment variables _

Override default values like so:

```python
bnet = BattleNet(
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

from django.http import HttpResponse, HttpResponseRedirect

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

def get_acces_token(request):

    if request.GET.get('code'):
        if request.GET.get('state') and request.session.get('state'):
            if request.GET['state'] == request.session['state']:
                bnet = BattleNetOAuth2()
                data = bnet.retrieve_access_token(request.GET['code'])
                if data.get('access_token'):
                    print data['access_token']

```

#### Request Battle.net Profile

```python

def get_bnet_profile(request):

    bnet = BattleNetOAuth2(scope='sc2.profile', access_token='access_token goes here')
    profile = bnet.get_profile(access_token='or here if you want to make multiple requests with same BNet object')
    print profile

```

#### Request Battletag

```python

def get_battletag(request):

    bnet = BattleNetOAuth2(access_token='access_token goes here')
    btag = bnet.get_battletag(access_token='or here')
    print btag

```

#### Request Account ID

```python

def get_accountid(request):

    bnet = BattleNetOAuth2(access_token='access_token goes here')
    account = bnet.get_account_id(access_token='or here')
    print account

```
