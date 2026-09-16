def get_p_vals(self, X):
    z_scores = self.get_scores(X[:, (0)], X[:, (1)])
    return norm.cdf(z_scores)