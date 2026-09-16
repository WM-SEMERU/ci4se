def score(self, testing_features, testing_target):
    if self.fitted_pipeline_ is None:
        raise RuntimeError(
            'A pipeline has not yet been optimized. Please call fit() first.')
    testing_features, testing_target = self._check_dataset(testing_features,
        testing_target, sample_weight=None)
    score = SCORERS[self.scoring_function](self.fitted_pipeline_,
        testing_features.astype(np.float64), testing_target.astype(np.float64))
    return score