def run_study(self, study, **kws):
    if not study:
        return []
    methods = Methods(kws['methods']) if 'methods' in kws else self.methods
    alpha = kws['alpha'] if 'alpha' in kws else self.alpha
    log = kws['log'] if 'log' in kws else self.log
    results = self.get_pval_uncorr(study, log)
    if not results:
        return []
    if log is not None:
        log.write('  {MSG}\n'.format(MSG='\n  '.join(self.get_results_msg(
            results, study))))
    self._run_multitest_corr(results, methods, alpha, study, log)
    for rec in results:
        rec.set_goterm(self.obo_dag)
    if 'keep_if' in kws:
        keep_if = kws['keep_if']
        results = [r for r in results if keep_if(r)]
    results.sort(key=lambda r: [r.enrichment, r.NS, r.p_uncorrected])
    return results