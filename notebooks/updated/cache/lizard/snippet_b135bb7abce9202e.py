def sample_stats_prior_to_xarray(self):
    dtypes = {'divergent__': bool, 'n_leapfrog__': np.int64, 'treedepth__':
        np.int64}
    dims = deepcopy(self.dims) if self.dims is not None else {}
    coords = deepcopy(self.coords) if self.coords is not None else {}
    sampler_params = self.sample_stats_prior
    for j, s_params in enumerate(sampler_params):
        rename_dict = {}
        for key in s_params:
            key_, *end = key.split('.')
            name = re.sub('__$', '', key_)
            name = 'diverging' if name == 'divergent' else name
            rename_dict[key] = '.'.join((name, *end))
            sampler_params[j][key] = s_params[key].astype(dtypes.get(key))
        sampler_params[j] = sampler_params[j].rename(columns=rename_dict)
    data = _unpack_dataframes(sampler_params)
    return dict_to_dataset(data, coords=coords, dims=dims)