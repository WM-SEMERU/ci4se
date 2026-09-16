def allocate(self):
    df = self.manager.get_historic_data()[self.SUPPORTED_COINS]
    change_columns = []
    for column in df:
        if column in self.SUPPORTED_COINS:
            change_column = '{}_change'.format(column)
            values = pd.Series((df[column].shift(-1) - df[column]) / -df[
                column].shift(-1)).values
            df[change_column] = values
            change_columns.append(change_column)
    columns = change_columns
    risks = df[columns].apply(np.nanvar, axis=0)
    returns = df[columns].apply(np.nanmean, axis=0)
    cov_matrix = df[columns].cov()
    cov_matrix.values[[np.arange(len(self.SUPPORTED_COINS))] * 2] = df[columns
        ].apply(np.nanvar, axis=0)
    weights = np.array([1 / len(self.SUPPORTED_COINS)] * len(self.
        SUPPORTED_COINS)).reshape(len(self.SUPPORTED_COINS), 1)
    min_risk = self.get_min_risk(weights, cov_matrix)
    min_return = np.dot(min_risk, returns.values)
    max_return = self.get_max_return(weights, returns)
    frontier = self.efficient_frontier(returns, cov_matrix, min_return,
        max_return, 6)
    return frontier