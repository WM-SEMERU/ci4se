def _update_estimate_and_sampler(self, ell, ell_hat, weight, extra_info, **
    kwargs):
    self._TP += ell_hat * ell * weight
    self._FP += ell_hat * (1 - ell) * weight
    self._FN += (1 - ell_hat) * ell * weight
    self._TN += (1 - ell_hat) * (1 - ell) * weight
    self._estimate[self.t_] = self._F_measure(self.alpha, self._TP, self.
        _FP, self._FN)