from battlenet.community import Community

class Career(Community):

    ENDPOINT = "/d3/profile/%s/"

    def __init__(self, *args, **kwargs):
        super(Career, self).__init__(*args, **kwargs)
        self.battletag = kwargs.get('battletag')

    def get(self, battletag=None):
        if battletag:
            self.battletag = battletag
        if not self.battletag:
            raise ValueError("BattleTag required.")

        return self.make_request(self.ENDPOINT % self.battletag)