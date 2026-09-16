def _bot(self, k):
    if k < 2:
        raise ValueError('k smaller than 2')
    G = np.ones((self.m, self.m))
    np.fill_diagonal(G, 0)
    for i in range(self.m):
        for j in range(self.m):
            if i == j:
                continue
            if i <= k and j <= k:
                G[i][j] = 0
    return G