def grad(self, X, *params):
    N = X.shape[0]
    D = self.get_dim(X)
    endinds = self.__base_locations(X)
    args = list(params)

    def make_dPhi(i, g):
        dPhi_dim = (N, D) if g.ndim < 3 else (N, D, g.shape[2])
        dPhi = np.zeros(dPhi_dim)
        dPhi[:, endinds[i]:endinds[i + 1]] = g
        return dPhi
    for i, base in enumerate(self.bases):
        g, args, sargs = base._grad_popargs(X, *args)
        for gg in atleast_tuple(g):
            if len(gg) == 0:
                continue
            yield make_dPhi(i, gg)