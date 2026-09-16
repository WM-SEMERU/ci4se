def get_mean_and_stddevs(self, sites, rup, dists, imt, stddev_types):
    C = self.COEFFS[imt]
    mag = self._convert_magnitude(rup.mag)
    f1 = self._compute_magnitude_scaling_term(C, mag)
    f2 = self._compute_geometrical_spreading_term(C, dists.rrup)
    f3 = self._compute_anelastic_attenuation_term(C, dists.rrup, mag)
    mean = f1 + f2 + f3
    mean = self._clip_mean(imt, mean)
    stddevs = self._get_stddevs(C, stddev_types, num_sites=len(dists.rrup),
        mag=mag)
    return mean, stddevs