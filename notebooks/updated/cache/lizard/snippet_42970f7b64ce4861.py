def _adjust_weights_by_phi_components(self, components, original_ceiling):
    obs = self.observation_data
    nz_groups = obs.groupby(obs['weight'].map(lambda x: x == 0)).groups
    ogroups = obs.groupby('obgnme').groups
    for ogroup, idxs in ogroups.items():
        if self.control_data.pestmode.startswith('regul'
            ) and 'regul' in ogroup.lower():
            continue
        og_phi = components[ogroup]
        nz_groups = obs.loc[(idxs), :].groupby(obs.loc[idxs, 'weight'].map(
            lambda x: x == 0)).groups
        og_nzobs = 0
        if False in nz_groups.keys():
            og_nzobs = len(nz_groups[False])
        if og_nzobs == 0 and og_phi > 0:
            raise Exception(
                'Pst.adjust_weights_by_phi_components(): no obs with nonzero weight,'
                 + ' but phi > 0 for group:' + str(ogroup))
        if og_phi > 0:
            factor = np.sqrt(float(og_nzobs) / float(og_phi))
            if original_ceiling:
                factor = min(factor, 1.0)
            obs.loc[idxs, 'weight'] = obs.weight[idxs] * factor
    self.observation_data = obs