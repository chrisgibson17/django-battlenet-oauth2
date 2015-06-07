from battlenet.community import Community

class Artisan(Community):

    ENDPOINT = "/d3/data/artisan/%s"

    def __init__(self, *args, **kwargs):
        super(Artisan, self).__init__(*args, **kwargs)
        self.artisan_data = kwargs.get('artisan_data')

    def get(self, artisan_data=None):
        if artisan_data:
            self.artisan_data = artisan_data
        if not self.artisan_data:
            raise ValueError("Artisan string required.")

        return self.make_request(self.ENDPOINT % self.artisan_data)
