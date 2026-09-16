def to_pandas_series_rdd(self):
    pd_index = self.index().to_pandas_index()
    return self.map(lambda x: (x[0], pd.Series(x[1], pd_index)))