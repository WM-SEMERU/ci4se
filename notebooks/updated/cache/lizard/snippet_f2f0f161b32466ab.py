def idxmin(self, **kwargs):
    if self._is_transposed:
        kwargs['axis'] = kwargs.get('axis', 0) ^ 1
        return self.transpose().idxmin(**kwargs)
    axis = kwargs.get('axis', 0)
    index = self.index if axis == 0 else self.columns

    def idxmin_builder(df, **kwargs):
        if axis == 0:
            df.index = index
        else:
            df.columns = index
        return df.idxmin(**kwargs)
    func = self._build_mapreduce_func(idxmin_builder, **kwargs)
    return self._full_axis_reduce(axis, func)