def aic(self):
    r
    aics = []
    aics_bool = []
    for i, chain in enumerate(self.parent.chains):
        p, n_data, n_free = (chain.posterior, chain.num_eff_data_points,
            chain.num_free_params)
        if p is None or n_data is None or n_free is None:
            aics_bool.append(False)
            missing = ''
            if p is None:
                missing += 'posterior, '
            if n_data is None:
                missing += 'num_eff_data_points, '
            if n_free is None:
                missing += 'num_free_params, '
            self._logger.warn(
                'You need to set %s for chain %s to get the AIC' % (missing
                [:-2], chain.name))
        else:
            aics_bool.append(True)
            c_cor = 1.0 * n_free * (n_free + 1) / (n_data - n_free - 1)
            aics.append(2.0 * (n_free + c_cor - np.max(p)))
    if len(aics) > 0:
        aics -= np.min(aics)
    aics_fin = []
    i = 0
    for b in aics_bool:
        if not b:
            aics_fin.append(None)
        else:
            aics_fin.append(aics[i])
            i += 1
    return aics_fin