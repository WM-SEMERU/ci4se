def predict_proba(self, features):
    if not self.fitted_pipeline_:
        raise RuntimeError(
            'A pipeline has not yet been optimized. Please call fit() first.')
    else:
        if not hasattr(self.fitted_pipeline_, 'predict_proba'):
            raise RuntimeError(
                'The fitted pipeline does not have the predict_proba() function.'
                )
        features = self._check_dataset(features, target=None, sample_weight
            =None)
        return self.fitted_pipeline_.predict_proba(features)