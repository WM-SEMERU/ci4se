def _fit_bmr_model(self, X, y):
    self.f_bmr = BayesMinimumRiskClassifier()
    X_bmr = self.predict_proba(X)
    self.f_bmr.fit(y, X_bmr)
    return self