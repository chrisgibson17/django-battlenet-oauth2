django-battlenet-oauth2
=======================

Basic class for getting Access Token &amp; Account Information from battlenet

THIS LIBRARY IS NOT ASSOCIATED WITH OR ENDORSED BY BLIZZARD IN ANY WAY

Example:

```
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
