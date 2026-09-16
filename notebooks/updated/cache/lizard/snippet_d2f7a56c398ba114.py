def setup(self, bottom, top):
    params = eval(self.param_str)
    self.voc_dir = params['voc_dir']
    self.split = params['split']
    self.mean = np.array(params['mean'])
    self.random = params.get('randomize', True)
    self.seed = params.get('seed', None)
    if len(top) != 2:
        raise Exception('Need to define two tops: data and label.')
    if len(bottom) != 0:
        raise Exception('Do not define a bottom.')
    split_f = '{}/ImageSets/Segmentation/{}.txt'.format(self.voc_dir, self.
        split)
    self.indices = open(split_f, 'r').read().splitlines()
    self.idx = 0
    if 'train' not in self.split:
        self.random = False
    if self.random:
        random.seed(self.seed)
        self.idx = random.randint(0, len(self.indices) - 1)