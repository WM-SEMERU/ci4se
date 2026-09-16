def summary(self):
    res = (
        'nlive: {:d}\nniter: {:d}\nncall: {:d}\neff(%): {:6.3f}\nlogz: {:6.3f} +/- {:6.3f}'
        .format(self.nlive, self.niter, sum(self.ncall), self.eff, self.
        logz[-1], self.logzerr[-1]))
    print('Summary\n=======\n' + res)