def get_mean_and_stddevs(self, sites, rup, dists, imt, stddev_types):
    coeffs = self.COEFFS[imt]
    coeffs.update(self.CONSTS)
    log_mean = self._compute_magnitude(rup, coeffs) + self._compute_distance(
        dists, coeffs) + self._get_site_amplification(sites, coeffs
        ) + self._get_mechanism(rup, coeffs)
    mean = log_mean * np.log(10.0) - np.log(g)
    log_stddevs = self._get_stddevs(coeffs, stddev_types, len(sites.vs30))
    stddevs = log_stddevs * np.log(10.0)
    return mean, stddevs