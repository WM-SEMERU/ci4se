def eval_proxop(self, V):
    return np.asarray(sp.prox_l1(V, self.lmbda / self.L * self.wl1), dtype=
        self.dtype)