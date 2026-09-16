def _estimate_AIC(self, y, mu, weights=None):
    estimated_scale = not self.distribution._known_scale
    return -2 * self._loglikelihood(y=y, mu=mu, weights=weights
        ) + 2 * self.statistics_['edof'] + 2 * estimated_scale