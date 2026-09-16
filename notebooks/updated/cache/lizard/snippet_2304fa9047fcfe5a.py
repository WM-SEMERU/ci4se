def sample_stats_to_xarray(self):
    rename_key = {'model_logp': 'lp'}
    data = {}
    for stat in self.trace.stat_names:
        name = rename_key.get(stat, stat)
        data[name] = np.array(self.trace.get_sampler_stats(stat, combine=False)
            )
    log_likelihood, dims = self._extract_log_likelihood()
    if log_likelihood is not None:
        data['log_likelihood'] = log_likelihood
        dims = {'log_likelihood': dims}
    else:
        dims = None
    return dict_to_dataset(data, library=self.pymc3, dims=dims, coords=self
        .coords)