def roc_auc_cv(self, features, labels):
    if callable(getattr(self.ml, 'decision_function', None)):
        return np.mean([self.scoring_function(labels[test], self.pipeline.
            fit(features[train], labels[train]).decision_function(features[
            test])) for train, test in KFold().split(features, labels)])
    elif callable(getattr(self.ml, 'predict_proba', None)):
        return np.mean([self.scoring_function(labels[test], self.pipeline.
            fit(features[train], labels[train]).predict_proba(features[test
            ])[:, (1)]) for train, test in KFold().split(features, labels)])
    else:
        raise ValueError("ROC AUC score won't work with " + self.ml_type +
            '. No decision_function or predict_proba method found for this learner.'
            )