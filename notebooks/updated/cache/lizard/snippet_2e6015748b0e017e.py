def get_mean_and_stddevs(self, sites, rup, dists, imt, stddev_types):
    coeffs = self.COEFFS_BEDROCK[imt].copy()
    coeffs.update(self.CONSTS)
    ln_mean = self._compute_mean(rup, dists, coeffs)
    ln_stddev = self._get_stddevs(coeffs, stddev_types)
    return ln_mean, [ln_stddev]