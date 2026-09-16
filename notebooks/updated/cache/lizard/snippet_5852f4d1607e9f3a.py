def min_volatility(self):
    if not self.w:
        self.solve()
    var = []
    for w in self.w:
        a = np.dot(np.dot(w.T, self.cov_matrix), w)
        var.append(a)
    self.weights = self.w[var.index(min(var))].reshape((self.n_assets,))
    return dict(zip(self.tickers, self.weights))