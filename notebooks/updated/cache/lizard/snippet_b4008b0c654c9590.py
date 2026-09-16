def computePerturbedFreeEnergies(self, u_ln, compute_uncertainty=True,
    uncertainty_method=None, warning_cutoff=1e-10):
    u_ln = np.array(u_ln, dtype=np.float64)
    if len(np.shape(u_ln)) == 3:
        u_ln = kln_to_kn(u_ln, N_k=self.N_k)
    [L, N] = u_ln.shape
    if N < self.N:
        raise DataError(
            'There seems to be too few samples in u_kn. You must evaluate at the new potential with all of the samples used originally.'
            )
    state_list = np.arange(L)
    A_in = np.array([0])
    inner_results = self.computeExpectationsInner(A_in, u_ln, state_list,
        return_theta=compute_uncertainty, uncertainty_method=
        uncertainty_method, warning_cutoff=warning_cutoff)
    Deltaf_ij, dDeltaf_ij = None, None
    f_k = np.matrix(inner_results['f'])
    result_vals = dict()
    result_vals['Delta_f'] = np.array(f_k - f_k.transpose())
    if compute_uncertainty:
        result_vals['dDelta_f'] = self._ErrorOfDifferences(inner_results[
            'Theta'], warning_cutoff=warning_cutoff)
    return result_vals