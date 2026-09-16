def get_mean_and_stddevs(self, sites, rup, dists, imt, stddev_types):
    C = self.COEFFS[imt]
    rhypo = dists.rhypo.copy()
    rhypo[rhypo < 10] = 10
    mag = (rup.mag * 0.98 - 0.39 if rup.mag <= 5.5 else 2.715 - 0.277 * rup
        .mag + 0.127 * rup.mag * rup.mag)
    f1 = np.minimum(np.log(rhypo), np.log(70.0))
    f2 = np.maximum(np.log(rhypo / 130.0), 0)
    mean = C['c1'] + C['c2'] * mag + C['c3'] * mag ** 2 + (C['c4'] + C['c5'
        ] * mag) * f1 + (C['c6'] + C['c7'] * mag) * f2 + C['c8'] * rhypo
    stddevs = self._get_stddevs(stddev_types, dists.rhypo.shape[0])
    return mean, stddevs