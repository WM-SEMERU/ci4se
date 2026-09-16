def f(self, X, test_data=False):
    X_warped = X.copy()
    if test_data:
        X_normalized = (X - self.Xmin) / (self.Xmax - self.Xmin)
    else:
        X_normalized = self.X_normalized
    for i_seq, i_fea in enumerate(self.warping_indices):
        a, b = self.params[i_seq][0], self.params[i_seq][1]
        X_warped[:, (i_fea)] = 1 - np.power(1 - np.power(X_normalized[:, (
            i_fea)], a), b)
    return X_warped