def propose_live(self):
    i = self.rstate.randint(self.nlive)
    u = self.live_u[(i), :]
    if self.sampling in ['rwalk', 'rstagger', 'rslice']:
        ax = self.ell.axes
    elif self.sampling == 'slice':
        ax = self.ell.paxes
    else:
        ax = np.identity(self.npdim)
    return u, ax