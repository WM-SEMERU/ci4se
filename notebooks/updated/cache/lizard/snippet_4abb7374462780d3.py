def fit(self, X, y, cost_mat, check_input=False):
    n_samples, self.n_features_ = X.shape
    self.tree_ = self._tree_class()
    if isinstance(self.max_features, six.string_types):
        if self.max_features == 'auto':
            max_features = max(1, int(np.sqrt(self.n_features_)))
        elif self.max_features == 'sqrt':
            max_features = max(1, int(np.sqrt(self.n_features_)))
        elif self.max_features == 'log2':
            max_features = max(1, int(np.log2(self.n_features_)))
        else:
            raise ValueError(
                'Invalid value for max_features. Allowed string values are "auto", "sqrt" or "log2".'
                )
    elif self.max_features is None:
        max_features = self.n_features_
    elif isinstance(self.max_features, (numbers.Integral, np.integer)):
        max_features = self.max_features
    elif self.max_features > 0.0:
        max_features = max(1, int(self.max_features * self.n_features_))
    else:
        max_features = 1
    self.max_features_ = max_features
    self.tree_.tree = self._tree_grow(y, X, cost_mat)
    if self.pruned:
        self.pruning(X, y, cost_mat)
    self.classes_ = np.array([0, 1])
    return self