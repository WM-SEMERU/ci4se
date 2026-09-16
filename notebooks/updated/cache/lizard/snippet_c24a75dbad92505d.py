def propose_unif(self):
    if self.use_kdtree:
        kdtree = spatial.KDTree(self.live_u)
    else:
        kdtree = None
    while True:
        u, q = self.radfriends.sample(self.live_u, rstate=self.rstate,
            return_q=True, kdtree=kdtree)
        if unitcheck(u, self.nonperiodic):
            if q == 1 or self.rstate.rand() < 1.0 / q:
                break
    ax = np.identity(self.npdim) * self.radfriends.radius
    return u, ax