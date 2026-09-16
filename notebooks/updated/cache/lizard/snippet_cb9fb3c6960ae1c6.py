def _build_features_caches(self):
    _donors_pool = self._donors_pool.get()[0]
    _lr_curves = self._lr_curves.get()[0]
    if _donors_pool is None or _lr_curves is None:
        return None
    self.num_donors = len(_donors_pool)
    self.continuous_features = np.zeros((self.num_donors, len(
        CONTINUOUS_FEATURES)))
    for idx, d in enumerate(_donors_pool):
        features = [d.get(specified_key) for specified_key in
            CONTINUOUS_FEATURES]
        self.continuous_features[idx] = features
    self.categorical_features = np.zeros((self.num_donors, len(
        CATEGORICAL_FEATURES)), dtype='object')
    for idx, d in enumerate(_donors_pool):
        features = [d.get(specified_key) for specified_key in
            CATEGORICAL_FEATURES]
        self.categorical_features[idx] = np.array([features], dtype='object')
    self.logger.info('Reconstructed matrices for similarity recommender')