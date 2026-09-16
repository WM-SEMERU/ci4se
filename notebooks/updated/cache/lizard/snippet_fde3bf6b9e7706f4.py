def toc(self):
    elapsed = self._time() - self.tstart
    if self.verbose:
        self.write('...toc(%r)=%.4fs\n' % (self.label, elapsed))
        self.flush()
    return elapsed