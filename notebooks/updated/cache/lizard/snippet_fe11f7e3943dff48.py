def fit(self, X, y=None):
    logger.info('Starting Deterministic SRM')
    if len(X) <= 1:
        raise ValueError(
            'There are not enough subjects ({0:d}) to train the model.'.
            format(len(X)))
    if X[0].shape[1] < self.features:
        raise ValueError(
            'There are not enough samples to train the model with {0:d} features.'
            .format(self.features))
    number_trs = X[0].shape[1]
    number_subjects = len(X)
    for subject in range(number_subjects):
        assert_all_finite(X[subject])
        if X[subject].shape[1] != number_trs:
            raise ValueError('Different number of samples between subjects.')
    self.w_, self.s_ = self._srm(X)
    return self