def coef_(self):
    coef = numpy.zeros(self.n_features_ + 1, dtype=float)
    for estimator in self.estimators_:
        coef[estimator.component] += self.learning_rate * estimator.coef_
    return coef