def autoscale_eydata(self):
    if not self.results:
        self._error('You must complete a fit first.')
        return
    r = self.reduced_chi_squareds()
    for n in range(len(r)):
        self['scale_eydata'][n] *= _n.sqrt(r[n])
    self.clear_results()
    if self['autoplot']:
        self.plot()
    return self