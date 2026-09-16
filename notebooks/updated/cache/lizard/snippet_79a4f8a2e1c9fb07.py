def get_mean_and_stddevs(self, sites, rup, dists, imt, stddev_types):
    C = self.COEFFS[imt]
    M = rup.mag - 6
    R = np.sqrt(dists.rjb ** 2 + C['h'] ** 2)
    gamma = np.array([(0 if v > 910.0 else 1) for v in sites.vs30])
    mean = np.zeros_like(R)
    mean += C['b1'] + C['b2'] * M + C['b3'] * M ** 2 + C['b5'] * np.log10(R
        ) + C['b6'] * gamma
    mean /= np.log10(np.e)
    if imt != PGA() and imt != PGV():
        omega = 2.0 * np.pi / imt.period
        mean += np.log(omega / (gravity * 100))
    stddevs = self._get_stddevs(C, stddev_types, dists.rjb.shape[0])
    stddevs = [(sd / np.log10(np.e)) for sd in stddevs]
    return mean, stddevs