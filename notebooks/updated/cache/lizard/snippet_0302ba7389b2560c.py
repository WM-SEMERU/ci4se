def instantaneous_tpole(self):
    logger.debug('{}.instantaneous_tpole'.format(self.component))
    if 'tpole' not in self.inst_vals.keys():
        logger.debug('{}.instantaneous_tpole COMPUTING'.format(self.component))
        if self.mesh is None:
            raise ValueError('mesh must be computed before determining tpole')
        self.inst_vals['tpole'] = self.teff * (np.sum(self.mesh.areas) / np
            .sum(self.mesh.gravs.centers * self.mesh.areas)) ** 0.25
    return self.inst_vals['tpole']