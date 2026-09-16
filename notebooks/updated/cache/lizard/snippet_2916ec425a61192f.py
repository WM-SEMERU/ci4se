def quantile_for_single_value(self, **kwargs):
    if self._is_transposed:
        kwargs['axis'] = kwargs.get('axis', 0) ^ 1
        return self.transpose().quantile_for_single_value(**kwargs)
    axis = kwargs.get('axis', 0)
    q = kwargs.get('q', 0.5)
    assert type(q) is float

    def quantile_builder(df, **kwargs):
        try:
            return pandas.DataFrame.quantile(df, **kwargs)
        except ValueError:
            return pandas.Series()
    func = self._build_mapreduce_func(quantile_builder, **kwargs)
    result = self._full_axis_reduce(axis, func)
    if axis == 0:
        result.index = [q]
    else:
        result.columns = [q]
    return result