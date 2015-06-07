from battlenet.community import Community

class Hero(Community):

    ENDPOINT = "/d3/profile/%s/hero/%s/"

    def __init__(self, *args, **kwargs):
        super(Hero, self).__init__(*args, **kwargs)
        self.battletag = kwargs.get('battletag')
        self.hero_id = kwargs.get('hero_id')

    def get(self, battletag=None, hero_id=None):
        if battletag:
            self.battletag = battletag
        if hero_id:
            self.hero_id = hero_id
        if not self.battletag:
            raise ValueError("BattleTag required.")
        if not self.hero_id:
            raise ValueError("Hero ID required"

        return self.make_request(self.ENDPOINT % (self.battletag, self.hero_id))