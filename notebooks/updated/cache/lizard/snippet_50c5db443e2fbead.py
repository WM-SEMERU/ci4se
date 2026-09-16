def read_random_state(self, group=None):
    group = self.sampler_group if group is None else group
    dataset_name = '/'.join([group, 'random_state'])
    arr = self[dataset_name][:]
    s = self[dataset_name].attrs['s']
    pos = self[dataset_name].attrs['pos']
    has_gauss = self[dataset_name].attrs['has_gauss']
    cached_gauss = self[dataset_name].attrs['cached_gauss']
    return s, arr, pos, has_gauss, cached_gauss