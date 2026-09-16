def _update_pi_vars(self):
    with scipy.errstate(divide='raise', under='raise', over='raise',
        invalid='raise'):
        for r in range(self.nsites):
            self.pi_codon[r] = self.pi[r][CODON_TO_AA]
            pim = scipy.tile(self.pi_codon[r], (N_CODON, 1))
            self.piAx_piAy[r] = pim.transpose() / pim
        self.ln_pi_codon = scipy.log(self.pi_codon)
        self.piAx_piAy_beta = self.piAx_piAy ** self.beta
        self.ln_piAx_piAy_beta = scipy.log(self.piAx_piAy_beta)