django-battlenet-oauth2
=======================

Basic class for getting Access Token &amp; Account Information from battlenet

THIS LIBRARY IS NOT ASSOCIATED WITH, OR ENDORSED BY, BLIZZARD IN ANY WAY.

##Installation (Only tested on OSX but I assume Windows is the same/simailar)

Clone the repo: git clone git@github.com:chrisgibson17/django-battlenet-oauth2.git (or use GitHub client)

Navigate to the local repo and run: (sudo) python setup.py install

_Some caveats before you look at the example:_

* `state_generator()` is for testing/example purposes only.  DO NOT USE THIS IN PRODUCTION.

From the [Battle.net docs](https://dev.battle.net/docs/read/oauth):

```
State Parameter

When requesting an authorization code (by directing the player to battle.net), one of the
parameters you should pass is the state parameter. To us, this is an opaque blob, but should
be semi-random to help prevent cross-site scripting attacks. Otherwise, an evil hacker could
direct someone to us, who direct to you, which causes you to do some action that the user
didn't actually request. In addition, since the data is sent back to you untransformed, this
can be used as a way for you to manage multiple redirect locations...but if not properly
secured, could be used to redirect a user to a phishing site or other evil purpose because
the redirect location wasn't checked.

```

* I use http://docs.python-requests.org/ for HTTP requests.  Install by: pip install requests
    - I'm using version 2.0.0 but any 2.* should work. (Current is 2.3)

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


#### Overriding default values
These can be overridden in the constructor like so:

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

N.B. It is recommended that your Key & Secret are stored as environment variables rather than in your codebase

##Example:

```python

from django.http import HttpResponse

from battlenet import BattleNet

from requests.exceptions import HTTPError

def register(request):

    def state_generator(size=8, chars=string.ascii_uppercase + string.digits):
        return ''.join(random.choice(chars) for _ in range(size))

    if request.GET.get('error'):
        return HttpResponse(request.GET['error_description'])

    bnet = BattleNet()

    if not request.GET.get('code'):
        return bnet.redirect_to_authorization(state_generator())

    try:
        data = bnet.retrieve_access_token(request.GET['code'])
    except HTTPError as e:
        print e.response.status_code
        print e.response.json()
        assert False

    # do stuff with access token etc (save)

    try:
        profile_data = bnet.get_battlenet_profile()
        return HttpResponse(str(profile_data))
    except HTTPError as e:
        print e.response.status_code
        print e.response.json()
        assert False

    return HttpResponse("Something is broken...")
```
