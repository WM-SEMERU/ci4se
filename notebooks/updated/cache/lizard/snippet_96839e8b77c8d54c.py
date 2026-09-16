def _col_type_set(self, col, df):
    type_set = set()
    if df[col].dtype == np.dtype(object):
        unindexed_col = list(df[col])
        for i in range(0, len(df[col])):
            if unindexed_col[i] == np.nan:
                continue
            else:
                type_set.add(type(unindexed_col[i]))
        return type_set
    else:
        type_set.add(df[col].dtype)
        return type_set