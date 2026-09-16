def check_valid_values(function):

    def decorated(self, X, *args, **kwargs):
        if isinstance(X, pd.DataFrame):
            W = X.values
        else:
            W = X
        if not len(W):
            raise ValueError('Your dataset is empty.')
        if W.dtype not in [np.dtype('float64'), np.dtype('int64')]:
            raise ValueError('There are non-numerical values in your data.')
        if np.isnan(W).any().any():
            raise ValueError('There are nan values in your data.')
        return function(self, X, *args, **kwargs)
    return decorated