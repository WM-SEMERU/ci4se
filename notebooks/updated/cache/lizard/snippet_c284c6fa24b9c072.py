def _pairwise_corr(self, columns=None, covar=None, tail='two-sided', method
    ='pearson', padjust='none', export_filename=None):
    stats = pairwise_corr(data=self, columns=columns, covar=covar, tail=
        tail, method=method, padjust=padjust, export_filename=export_filename)
    return stats