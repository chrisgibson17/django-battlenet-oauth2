from battlenet.community import Community

class Data(Community):
    def get(self):
        return self.make_request(self.ENDPOINT)

class BattleGroups(Data):
    ENDPOINT = '/wow/data/battlegroups/'

class CharacterRaces(Data):
    ENDPOINT = '/wow/data/character/races'

class CharacterClasses(Data):
    ENDPOINT = '/wow/data/character/classes'

class CharacterAchievements(Data):
    ENDPOINT = '/wow/data/character/achievements'

class GuildAchievements(Data):
    ENDPOINT = '/wow/data/guild/achievements'

class GuildRewards(Data):
    ENDPOINT = '/wow/data/guild/rewards'

class GuildPerks(Data):
    ENDPOINT = '/wow/data/guild/perks'

class ItemClasses(Data):
    ENDPOINT = '/wow/data/item/classes'

class Talents(Data):
    ENDPOINT = '/wow/data/talents'

class PetTypes(Data):
    ENDPOINT = '/wow/data/pet/types'