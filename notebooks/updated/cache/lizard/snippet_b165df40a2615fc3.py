def computeEffectiveSampleNumber(self, verbose=False):
    N_eff = np.zeros(self.K)
    for k in range(self.K):
        w = np.exp(self.Log_W_nk[:, (k)])
        N_eff[k] = 1 / np.sum(w ** 2)
        if verbose:
            print('Effective number of sample in state %d is %10.3f' % (k,
                N_eff[k]))
            print('Efficiency for state %d is %d/%d = %10.4f' % (k, N_eff[k
                ], len(w), N_eff[k] / len(w)))
    return N_eff