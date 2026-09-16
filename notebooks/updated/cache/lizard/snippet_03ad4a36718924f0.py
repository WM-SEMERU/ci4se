def _compute_Lp_matrix(self):
    self.Lp = sum([(1 / self.eigen_values[i] * np.outer(self.eigen_basis[:,
        (i)], self.eigen_basis[:, (i)])) for i in range(1, self.
        eigen_values.size)])