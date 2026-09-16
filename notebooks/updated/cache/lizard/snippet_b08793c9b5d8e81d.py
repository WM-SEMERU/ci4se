def get_mean_and_stddevs(self, sites, rup, dists, imt, stddev_types):
    C = self.COEFFS[imt]
    mag = rup.mag - 6
    d = np.sqrt(dists.rjb ** 2 + C['c7'] ** 2)
    mean = np.zeros_like(d)
    mean += C['c1'] + C['c2'] * mag + C['c3'] * mag ** 2 + C['c6']
    idx = d <= 100.0
    mean[idx] = mean[idx] + C['c5'] * np.log10(d[idx])
    idx = d > 100.0
    mean[idx] = mean[idx] + C['c5'] * np.log10(100.0) - np.log10(d[idx] / 100.0
        ) + C['c4'] * (d[idx] - 100.0)
    mean = np.log(10.0 ** (mean - 2.0) / g)
    stddevs = self._get_stddevs(C, stddev_types, dists.rjb.shape[0])
    return mean, stddevs