def get_nsing(self, epsilon=0.0001):
    mx = self.xtqx.shape[0]
    nsing = mx - np.searchsorted(np.sort((self.xtqx.s.x / self.xtqx.s.x.max
        ())[:, (0)]), epsilon)
    if nsing == mx:
        self.logger.warn('optimal nsing=npar')
        nsing = None
    return nsing