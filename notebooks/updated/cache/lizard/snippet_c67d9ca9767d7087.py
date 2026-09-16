def _compute_dk_dtau(self, tau, n):
    r
    deriv_pattern = []
    for idx in xrange(0, len(n)):
        deriv_pattern.extend(n[idx] * [idx])
    deriv_pattern = scipy.asarray(deriv_pattern, dtype=int)
    if len(deriv_pattern) == 0:
        return self._compute_k(tau)
    else:
        deriv_partitions = generate_set_partitions(deriv_pattern)
        dk_dtau = scipy.zeros(tau.shape[0])
        for partition in deriv_partitions:
            dk_dtau += self._compute_dk_dtau_on_partition(tau, partition)
        return dk_dtau