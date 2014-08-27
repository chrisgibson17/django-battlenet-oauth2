from battlenet.community import Community

class Quest(Community):

    ENDPOINT = '/wow/quest/%s'
    def __init__(self, *args, **kwargs):
        super(Quest, self).__init__(*args, **kwargs)
        self.quest = kwargs.get('quest')

    def get(self, quest=None):
        if quest:
            self.quest = quest
        else:
            if not self.quest:
                raise ValueError('Quest ID required.')

        return self.make_request(self.ENDPOINT % self.quest)