def sample(self, rstate=None):
    if rstate is None:
        rstate = np.random
    return rstate.rand(self.n)