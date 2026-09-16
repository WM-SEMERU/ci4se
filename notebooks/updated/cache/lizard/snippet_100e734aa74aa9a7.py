def cric__random_forest():
    model = sklearn.ensemble.RandomForestClassifier(100, random_state=0)
    model.predict = lambda X: model.predict_proba(X)[:, (1)]
    return model