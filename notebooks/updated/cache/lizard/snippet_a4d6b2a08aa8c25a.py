def get_num_sig(self, alpha=0.05):
    ctr = cx.Counter()
    flds = set(['FDR', 'Bonferroni', 'Benjamini', 'PValue'])
    for ntd in self.nts:
        for fld in flds:
            if getattr(ntd, fld) < alpha:
                ctr[fld] += 1
    return ctr