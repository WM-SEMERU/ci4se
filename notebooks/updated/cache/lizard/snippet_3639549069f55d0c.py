def update_cov(self):
    scaling = 2.4 ** 2 / self.dim
    epsilon = 1e-05
    chain = np.asarray(self._trace)
    self.C, self.chain_mean = self.recursive_cov(self.C, self._trace_count,
        self.chain_mean, chain, scaling=scaling, epsilon=epsilon)
    acc_rate = self.accepted / (self.accepted + self.rejected)
    if self.shrink_if_necessary:
        if acc_rate < 0.001:
            self.C *= 0.01
        elif acc_rate < 0.01:
            self.C *= 0.25
        if self.verbose > 1:
            if acc_rate < 0.01:
                print_('\tAcceptance rate was', acc_rate,
                    'shrinking covariance')
    self.accepted = 0.0
    self.rejected = 0.0
    if self.verbose > 1:
        print_('\tUpdating covariance ...\n', self.C)
        print_('\tUpdating mean ... ', self.chain_mean)
    adjustmentwarning = ('\n' +
        """Covariance was not positive definite and proposal_sd cannot be computed by 
"""
         +
        'Cholesky decomposition. The next jumps will be based on the last \n' +
        """valid covariance matrix. This situation may have arisen because no 
"""
         +
        'jumps were accepted during the last `interval`. One solution is to \n'
         +
        """increase the interval, or specify an initial covariance matrix with 
"""
         +
        'a smaller variance. For this simulation, each time a similar error \n'
         +
        """occurs, proposal_sd will be reduced by a factor .9 to reduce the 
"""
         + 'jumps and increase the likelihood of accepted jumps.')
    try:
        self.updateproposal_sd()
    except np.linalg.LinAlgError:
        warnings.warn(adjustmentwarning)
        self.covariance_adjustment(0.9)
    self._trace_count += len(self._trace)
    self._trace = []