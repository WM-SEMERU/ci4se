def first_valid_index(self):

    def first_valid_index_builder(df):
        df.index = pandas.RangeIndex(len(df.index))
        return df.apply(lambda df: df.first_valid_index())
    func = self._build_mapreduce_func(first_valid_index_builder)
    first_result = self._full_axis_reduce(0, func).min(axis=1).to_pandas(
        ).squeeze()
    return self.index[first_result]