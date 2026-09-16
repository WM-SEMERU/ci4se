def predict_noiseless(self, Xnew, full_cov=False, Y_metadata=None, kern=None):
    return self.predict(Xnew, full_cov, Y_metadata, kern, None, False)