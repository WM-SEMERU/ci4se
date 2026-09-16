def aggregate(self, index):
    if isinstance(index, string_types):
        col_df_grouped = self.col_df.groupby(self.df[index])
    else:
        self.col_df.index = pd.MultiIndex.from_arrays([self.df[i] for i in
            index])
        col_df_grouped = self.col_df.groupby(level=index)
        self.col_df.index = self.df.index
    self.reduced_df = pd.DataFrame({colred: col_df_grouped[colred.column].
        agg(colred.agg_func) for colred in self.column_reductions})
    reduced_dfs = []
    for cf in self.column_functions:
        reduced_dfs.append(cf.apply_and_name(self))
    return pd.concat(reduced_dfs, axis=1)