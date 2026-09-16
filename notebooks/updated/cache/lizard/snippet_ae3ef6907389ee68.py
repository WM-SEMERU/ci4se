def fit(self, X, y, random_state=np.random):
    if self.num_labeled != 'deprecated':
        warnings.warn(
            '"num_labeled" parameter is not used. It has been deprecated in version 0.5.0 and will beremoved in 0.6.0'
            , DeprecationWarning)
    X, y = self._prepare_inputs(X, y, ensure_min_samples=2)
    num_constraints = self.num_constraints
    if num_constraints is None:
        num_classes = len(np.unique(y))
        num_constraints = 20 * num_classes ** 2
    c = Constraints(y)
    pos_neg = c.positive_negative_pairs(num_constraints, random_state=
        random_state)
    pairs, y = wrap_pairs(X, pos_neg)
    return _BaseMMC._fit(self, pairs, y)