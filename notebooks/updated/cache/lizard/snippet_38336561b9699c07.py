def transform(self, X, y=None):
    if not X.columns.equals(self.columns_):
        raise ValueError(
            "Columns of 'X' do not match the training columns. Got {!r}, expected {!r}"
            .format(X.columns, self.columns))
    if not isinstance(X, (pd.DataFrame, dd.DataFrame)):
        raise TypeError('Unexpected type {}'.format(type(X)))
    X = X.copy()
    for col in self.categorical_columns_:
        X[col] = X[col].cat.codes
    return X