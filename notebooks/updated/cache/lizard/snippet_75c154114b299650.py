def apply_correlation(self, sites, imt, residuals, stddev_intra):
    if stddev_intra.shape[0] == 1:
        stddev_intra = numpy.matlib.repmat(stddev_intra, len(sites.complete), 1
            )
    stddev_intra = stddev_intra.squeeze()
    if not stddev_intra.shape:
        stddev_intra = stddev_intra[None]
    if self.uncertainty_multiplier == 0:
        residuals_norm = residuals / stddev_intra[sites.sids, None]
        try:
            cormaLow = self.cache[imt]
        except KeyError:
            cormaLow = numpy.linalg.cholesky(numpy.diag(stddev_intra[sites.
                sids]) * self._get_correlation_matrix(sites, imt) * numpy.
                diag(stddev_intra[sites.sids]))
            self.cache[imt] = cormaLow
        return numpy.dot(cormaLow, residuals_norm)
    else:
        nsim = len(residuals[1])
        nsites = len(residuals)
        residuals_correlated = residuals * 0
        for isim in range(0, nsim):
            corma = self._get_correlation_matrix(sites, imt)
            cov = numpy.diag(stddev_intra[sites.sids]) * corma * numpy.diag(
                stddev_intra[sites.sids])
            residuals_correlated[0:, (isim)
                ] = numpy.random.multivariate_normal(numpy.zeros(nsites),
                cov, 1)
        return residuals_correlated