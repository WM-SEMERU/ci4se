def nnz_obs_names(self):
    obs = self.observation_data
    nz_names = list(obs.loc[obs.weight > 0.0, 'obsnme'])
    return nz_names