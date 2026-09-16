def _get_columns(self, X, cols):
    if isinstance(X, DataSet):
        X = X[cols]
    return_vector = False
    if isinstance(cols, basestring):
        return_vector = True
        cols = [cols]
    if isinstance(X, list):
        X = [x[cols] for x in X]
        X = pd.DataFrame(X)
    if return_vector:
        t = X[cols[0]]
    else:
        t = X.as_matrix(cols)
    return t