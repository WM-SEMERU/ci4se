def cric__ridge():
    model = sklearn.linear_model.LogisticRegression(penalty='l2')
    model.predict = lambda X: model.predict_proba(X)[:, (1)]
    return model