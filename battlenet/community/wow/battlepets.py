from battlenet.community import Community

class BattlePets(Community):

    ENDPOINT = '/wow/battlePet/%s/%s'
    AVAILABLE_DATASETS = [
        'ability',
        'species',
        'stats'
    ]
    optional_params = {
        'quality_id': None,
        'breed_id': None,
        'level': None
    }

    def __init__(self, *args, **kwargs):
        super(BattlePets, self).__init__(*args, **kwargs)
        if kwargs.get('dataset'):
            if kwargs['dataset'] not in self.AVAILABLE_DATASETS:
                raise ValueError('Invalid dataset provided. Options are "abilities", "species" or "stats".')
            self.dataset = kwargs['dataset']

        self.id = kwargs.get('id', None)

        if self.dataset is 'stats':
            if kwargs.get('level'):
                self.optional_params['level'] = kwargs['level']
            if kwargs.get('quality_id'):
                self.optional_params['quality_id'] = kwargs['quality_id']
            if kwargs.get('breed_id'):
                self.optional_params['breed_id'] = kwargs['breed_id']

    def get(self, dataset=None, id=None, level=None, breed_id=None, quality_id=None):
        if dataset:
            if dataset not in self.AVAILABLE_DATASETS:
                raise ValueError('Invalid dataset provided. Options are "abilities", "species" or "stats".')
            self.dataset = dataset
        else:
            if not self.dataset:
                raise ValueError('Data set required. Options are "abilities", "species" or "stats".')

        if id:
            self.id = id
        else:
            if not self.id:
                raise ValueError('Ability/Species ID required.')

        if self.dataset is 'stats':
            if level:
                self.optional_params['level'] = level
            if  quality_id:
                self.optional_params['qualityId'] = quality_id
            if breed_id:
                self.optional_params['breedId'] = breed_id

        final_params = {}
        for key, value in self.optional_params.iteritems():
            if value:
                final_params[key] = value

        if len(final_params) > 0:
            self.add_params(final_params)

        return self.make_request(self.ENDPOINT % (self.dataset, self.id))