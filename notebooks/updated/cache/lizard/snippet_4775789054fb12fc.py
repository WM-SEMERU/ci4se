def predict(self, X, categorical=None):
    assert hasattr(self, '_enc_cluster_centroids'), 'Model not yet fitted.'
    if categorical is not None:
        assert isinstance(categorical, (int, list, tuple)
            ), "The 'categorical'                 argument needs to be an integer with the index of the categorical                 column in your data, or a list or tuple of several of them,                 but it is a {}.".format(
            type(categorical))
    X = pandas_to_numpy(X)
    Xnum, Xcat = _split_num_cat(X, categorical)
    Xnum, Xcat = check_array(Xnum), check_array(Xcat, dtype=None)
    Xcat, _ = encode_features(Xcat, enc_map=self._enc_map)
    return _labels_cost(Xnum, Xcat, self._enc_cluster_centroids, self.
        num_dissim, self.cat_dissim, self.gamma)[0]