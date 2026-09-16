def get_mean_and_stddevs(self, sites, rup, dists, imt, stddev_types):
    C = self.COEFFS[imt]
    mean = np.log(self.get_magnitude_term(C, rup) + self.get_distance_term(
        C, dists.rrup)) + self.get_site_amplification(C, sites)
    stddevs = self.get_stddevs(C, sites.vs30.shape, rup.mag, stddev_types)
    return mean, stddevs