def randoffset(self, rstate=None):
    if rstate is None:
        rstate = np.random
    return np.dot(self.axes, randsphere(self.n, rstate=rstate))