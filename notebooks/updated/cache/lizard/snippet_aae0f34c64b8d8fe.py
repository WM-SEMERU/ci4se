def probability_density(self, X):
    self.check_fit()
    U, V = self.split_matrix(X)
    a = (self.theta + 1) * np.power(np.multiply(U, V), -(self.theta + 1))
    b = np.power(U, -self.theta) + np.power(V, -self.theta) - 1
    c = -(2 * self.theta + 1) / self.theta
    return a * np.power(b, c)