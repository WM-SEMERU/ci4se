def _get_path_scaling(self, C, dists, mag):
    rval = np.sqrt(dists.rjb ** 2.0 + C['h'] ** 2.0)
    scaling = (C['c1'] + C['c2'] * (mag - self.CONSTS['Mref'])) * np.log(
        rval / self.CONSTS['Rref'])
    return scaling + (C['c3'] + C['Dc3']) * (rval - self.CONSTS['Rref'])