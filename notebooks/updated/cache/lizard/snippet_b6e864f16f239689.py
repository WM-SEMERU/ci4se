def get_mean_and_stddevs(self, sites, rup, dists, imt, stddev_types):
    C = self.COEFFS[imt]
    C_PGA = self.COEFFS[PGA()]
    pga1100 = np.exp(self.get_mean_values(C_PGA, sites, rup, dists, None))
    mean = self.get_mean_values(C, sites, rup, dists, pga1100)
    if imt.name == 'SA' and imt.period <= 0.25:
        pga = self.get_mean_values(C_PGA, sites, rup, dists, pga1100)
        idx = mean <= pga
        mean[idx] = pga[idx]
    stddevs = self._get_stddevs(C, C_PGA, rup, sites, pga1100, stddev_types)
    return mean, stddevs