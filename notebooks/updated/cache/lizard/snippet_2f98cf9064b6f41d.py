def set_estimator_and_feature_spec(self, estimator, feature_spec):
    self.delete('custom_predict_fn')
    self.store('estimator_and_spec', {'estimator': estimator,
        'feature_spec': feature_spec})
    self.set_inference_address('estimator')
    if not self.has_model_name():
        self.set_model_name('1')
    return self