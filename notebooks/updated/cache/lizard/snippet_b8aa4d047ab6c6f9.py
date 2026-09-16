def fit(self, interactions, user_features=None, item_features=None,
    sample_weight=None, epochs=1, num_threads=1, verbose=False):
    self._reset_state()
    return self.fit_partial(interactions, user_features=user_features,
        item_features=item_features, sample_weight=sample_weight, epochs=
        epochs, num_threads=num_threads, verbose=verbose)