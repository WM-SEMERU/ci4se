def propose_live(self):
    i = self.rstate.randint(self.nlive)
    u = self.live_u[(i), :]
    ell_idxs = self.mell.within(u)
    nidx = len(ell_idxs)
    if nidx == 0:
        try:
            expected_vol = math.exp(self.saved_logvol[-1] - self.dlv)
        except:
            expected_vol = math.exp(-self.dlv)
        pointvol = expected_vol / self.nlive
        bound = self.update(pointvol)
        if self.save_bounds:
            self.bound.append(bound)
        self.nbound += 1
        self.since_update = 0
        ell_idxs = self.mell.within(u)
        nidx = len(ell_idxs)
    ell_idx = ell_idxs[self.rstate.randint(nidx)]
    if self.sampling in ['rwalk', 'rstagger', 'rslice']:
        ax = self.mell.ells[ell_idx].axes
    elif self.sampling == 'slice':
        ax = self.mell.ells[ell_idx].paxes
    else:
        ax = np.identity(self.npdim)
    return u, ax