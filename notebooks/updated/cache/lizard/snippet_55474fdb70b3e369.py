def paramsReport(self):
    report = {}
    for param in self._REPORTPARAMS:
        pvalue = getattr(self, param)
        if isinstance(pvalue, float):
            report[param] = pvalue
        elif isinstance(pvalue, scipy.ndarray) and pvalue.shape == (N_NT,):
            for w in range(N_NT - 1):
                report['{0}{1}'.format(param, INDEX_TO_NT[w])] = pvalue[w]
        elif isinstance(pvalue, scipy.ndarray) and pvalue.shape == (self.
            nsites, N_AA):
            for r in range(self.nsites):
                for a in range(N_AA):
                    report['{0}{1}{2}'.format(param, r + 1, INDEX_TO_AA[a])
                        ] = pvalue[r][a]
        else:
            raise ValueError('Unexpected param: {0}'.format(param))
    return report