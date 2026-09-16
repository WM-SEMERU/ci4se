def get_mean_and_stddevs(self, sites, rup, dists, imt, stddev_types):
    C = self.COEFFS[imt]
    mean = self._compute_mean(C, rup, dists, sites, imt)
    stddevs = self._get_stddevs(C, stddev_types, sites.vs30.shape[0])
    return mean, stddevs