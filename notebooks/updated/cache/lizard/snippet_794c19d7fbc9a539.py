def _init_pval_name(self, **kws):
    if 'pval_name' in kws:
        return kws['pval_name']
    if self.is_goterm:
        return 'p_{M}'.format(M=next(iter(self.go2res.values())).
            get_method_name())
    for fld in next(iter(self.go2res.values()))._fields:
        if fld[:2] == 'p_' and fld != 'p_uncorrected':
            return fld