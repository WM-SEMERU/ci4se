def faithful(return_X_y=True):
    faithful = pd.read_csv(PATH + '/faithful.csv', index_col=0)
    if return_X_y:
        y, x = np.histogram(faithful['eruptions'], bins=200)
        X = x[:-1] + np.diff(x) / 2
        return _clean_X_y(X, y)
    return faithful