def predict(self, Xnew, full_cov=False, kern=None, **kwargs):
    return self.predict_noiseless(Xnew, full_cov=full_cov, kern=kern)