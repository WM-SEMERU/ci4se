def fit(self, X, y=None):
    if self.metric != 'precomputed':
        X = check_array(X, accept_sparse='csr')
        self._raw_data = X
    elif issparse(X):
        X = check_array(X, accept_sparse='csr')
    else:
        check_precomputed_distance_matrix(X)
    kwargs = self.get_params()
    kwargs.pop('prediction_data', None)
    kwargs.update(self._metric_kwargs)
    (self.labels_, self.probabilities_, self.cluster_persistence_, self.
        _condensed_tree, self._single_linkage_tree, self._min_spanning_tree
        ) = hdbscan(X, **kwargs)
    if self.prediction_data:
        self.generate_prediction_data()
    return self