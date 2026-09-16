def get_res_stats(self, nonzero=True):
    res = self.res.copy()
    res.loc[:, ('obsnme')] = res.pop('name')
    res.index = res.obsnme
    if nonzero:
        obs = self.observation_data.loc[(self.nnz_obs_names), :]
    res = res.loc[(obs.obsnme), :]
    res.loc[:, ('weight')] = obs.weight
    res.loc[:, ('obsval')] = obs.obsval
    res.loc[:, ('obgnme')] = obs.obgnme
    res.pop('group')
    res.pop('measured')
    og_dict = {og: res.loc[res.obgnme == og, 'obsnme'] for og in res.obgnme
        .unique()}
    og_names = list(og_dict.keys())
    sfuncs = [self._stats_rss, self._stats_mean, self._stats_mae, self.
        _stats_rmse, self._stats_nrmse]
    snames = ['rss', 'mean', 'mae', 'rmse', 'nrmse']
    data = []
    for sfunc, sname in zip(sfuncs, snames):
        full = sfunc(res)
        groups = [full]
        for og in og_names:
            onames = og_dict[og]
            res_og = res.loc[(onames), :]
            groups.append(sfunc(res_og))
        data.append(groups)
    og_names.insert(0, 'all')
    df = pd.DataFrame(data, columns=og_names, index=snames)
    return df