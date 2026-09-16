def standardize_genes(self, inplace=False):
    matrix = self.center_genes(inplace=inplace)
    matrix.X[:, :] = matrix.X / np.tile(np.std(matrix.X, axis=1, ddof=1), (
        matrix.n, 1)).T
    return matrix