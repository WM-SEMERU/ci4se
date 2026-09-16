def get_mean_and_stddevs(self, sites, rup, dists, imt, stddev_types):
    R = np.sqrt(dists.rjb ** 2 + 11.29 ** 2)
    M = rup.mag - 6
    S = np.zeros(R.shape)
    S[sites.vs30 <= 200] = 1
    mean = 0.518 + 0.387 * M - np.log10(R) - 0.00256 * R + 0.335 * S
    mean /= np.log10(np.e)
    assert all(stddev_type in self.DEFINED_FOR_STANDARD_DEVIATION_TYPES for
        stddev_type in stddev_types)
    stddevs = [0.237 / np.log10(np.e) + np.zeros(R.shape)]
    return mean, stddevs