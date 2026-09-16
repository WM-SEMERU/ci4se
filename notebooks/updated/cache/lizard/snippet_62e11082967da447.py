def X(self, i, j=slice(None, None, None)):
    X1 = self.fpix[j] / self.norm[j].reshape(-1, 1)
    X = np.product(list(multichoose(X1.T, i + 1)), axis=1).T
    if self.X1N is not None:
        return np.hstack([X, self.X1N[j] ** (i + 1)])
    else:
        return X