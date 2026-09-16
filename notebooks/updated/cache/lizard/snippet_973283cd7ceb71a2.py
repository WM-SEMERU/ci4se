def fit(self, X, y, **args):
    self.errors = []
    for alpha in self.alphas:
        self.estimator.set_params(alpha=alpha)
        scores = self.score_method(self.estimator, X, y)
        self.errors.append(scores.mean())
    self.errors = np.array(self.errors)
    self.draw()
    return self