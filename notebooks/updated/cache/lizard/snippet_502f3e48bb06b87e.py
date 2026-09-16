def quantile(self, q=0.5, interpolation='linear'):
    self._check_percentile(q)
    df = self.to_frame()
    result = df.quantile(q=q, interpolation=interpolation, numeric_only=False)
    if result.ndim == 2:
        result = result.iloc[:, (0)]
    if is_list_like(q):
        result.name = self.name
        return self._constructor(result, index=Float64Index(q), name=self.name)
    else:
        return result.iloc[0]