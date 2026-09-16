def get_results_sig(self):
    print('{N:7,} of {M:,} results have uncorrected P-values <= {PVAL}=pval\n'
        .format(N=sum(1 for r in self.results_all if r.p_uncorrected < self
        .args.pval), M=len(self.results_all), PVAL=self.args.pval))
    pval_fld = self.get_pval_field()
    results = [r for r in self.results_all if getattr(r, pval_fld) <= self.
        args.pval]
    return results