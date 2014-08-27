from battlenet.community import Community

class Spell(Community):

    ENDPOINT = '/wow/spell/%s'
    def __init__(self, *args, **kwargs):
        super(Spell, self).__init__(*args, **kwargs)
        self.spell = kwargs.get('spell')

    def get(self, spell=None):
        if spell:
            self.spell = spell
        else:
            if not self.spell:
                raise ValueError('Spell ID required.')

        return self.make_request(self.ENDPOINT % self.spell)