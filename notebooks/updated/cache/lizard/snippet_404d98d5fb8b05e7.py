def fit(self, X, y, **kwargs):
    super(ResidualsPlot, self).fit(X, y, **kwargs)
    self.score(X, y, train=True)
    return self