from battlenet.community import Community

class Recipe(Community):

    ENDPOINT = '/wow/recipe/%s'
    def __init__(self, *args, **kwargs):
        super(Recipe, self).__init__(*args, **kwargs)
        self.recipie = kwargs.get('recipe')

    def get(self, recipe=None):
        if recipe:
            self.recipe = recipe
        else:
            if not self.recipe:
                raise ValueError('Recipe ID required.')

        return self.make_request(self.ENDPOINT % self.recipe)