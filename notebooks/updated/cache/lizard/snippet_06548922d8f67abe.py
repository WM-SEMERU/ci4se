def _adj(self, k):
    G = np.zeros((self.m, self.m))
    for i in range(self.m):
        for j in range(self.m):
            if i == j + 1 or j == i + 1:
                G[i][j] = 1
    return G