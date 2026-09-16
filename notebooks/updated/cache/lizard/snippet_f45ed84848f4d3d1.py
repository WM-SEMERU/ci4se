def adjust_weights_discrepancy(self, resfile=None, original_ceiling=True):
    if resfile is not None:
        self.resfile = resfile
        self.__res = None
    obs = self.observation_data.loc[(self.nnz_obs_names), :]
    swr = (self.res.loc[(self.nnz_obs_names), :].residual * obs.weight) ** 2
    factors = (1.0 / swr).apply(np.sqrt)
    if original_ceiling:
        factors = factors.apply(lambda x: 1.0 if x > 1.0 else x)
    self.observation_data.loc[self.nnz_obs_names, 'weight'] *= factors