def _converged(self):
    prior = self.global_prior_[0:self.prior_size]
    posterior = self.global_posterior_[0:self.prior_size]
    diff = prior - posterior
    max_diff = np.max(np.fabs(diff))
    if self.verbose:
        _, mse = self._mse_converged()
        diff_ratio = np.sum(diff ** 2) / np.sum(posterior ** 2)
        logger.info('htfa prior posterior max diff %f mse %f diff_ratio %f' %
            (max_diff, mse, diff_ratio))
    if max_diff > self.threshold:
        return False, max_diff
    else:
        return True, max_diff