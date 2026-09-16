def transform(self, X):
    utils.validation.check_is_fitted(self, 's_')
    if self.check_input:
        utils.check_array(X, dtype=[str, np.number])
    return self.row_coordinates(X)