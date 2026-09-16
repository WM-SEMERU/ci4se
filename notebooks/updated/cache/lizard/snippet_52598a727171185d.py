def set_custom_predict_fn(self, predict_fn):
    self.delete('estimator_and_spec')
    self.store('custom_predict_fn', predict_fn)
    self.set_inference_address('custom_predict_fn')
    if not self.has_model_name():
        self.set_model_name('1')
    return self