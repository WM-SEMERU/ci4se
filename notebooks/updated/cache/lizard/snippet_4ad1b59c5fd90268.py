def reindex(self, axis, labels, **kwargs):

    def reindex_builer(df, axis, old_labels, new_labels, **kwargs):
        if axis:
            while len(df.columns) < len(old_labels):
                df[len(df.columns)] = np.nan
            df.columns = old_labels
            new_df = df.reindex(columns=new_labels, **kwargs)
            new_df.columns = pandas.RangeIndex(len(new_df.columns))
            return new_df
        else:
            while len(df.index) < len(old_labels):
                df.loc[len(df.index)] = np.nan
            df.index = old_labels
            new_df = df.reindex(index=new_labels, **kwargs)
            new_df.reset_index(inplace=True, drop=True)
            return new_df
    old_labels = self.columns if axis else self.index
    new_index = self.index if axis else labels
    new_columns = labels if axis else self.columns
    func = self._prepare_method(lambda df: reindex_builer(df, axis,
        old_labels, labels, **kwargs))
    new_data = self._map_across_full_axis(axis, func)
    return self.__constructor__(new_data, new_index, new_columns)