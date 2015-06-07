from battlenet.community import Community

class Follower(Community):

    ENDPOINT = "/d3/data/follower/%s"

    def __init__(self, *args, **kwargs):
        super(Follower, self).__init__(*args, **kwargs)
        self.follower_data = kwargs.get('follower_data')

    def get(self, follower_data=None):
        if follower_data:
            self.follower_data = follower_data
        if not self.follower_data:
            raise ValueError("Follower string required.")

        return self.make_request(self.ENDPOINT % self.follower_data)
