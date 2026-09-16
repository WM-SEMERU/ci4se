def copy_missing_columns(df, ref_df):
    cols = ref_df.columns.difference(df.columns)
    _loc = ref_df.columns.get_loc
    l1, l2 = len(df), len(ref_df)
    if l1 >= l2 and l1 % l2 == 0:
        idx = np.tile(range(l2), l1 // l2)
    else:
        idx = np.repeat(0, l1)
    for col in cols:
        df[col] = ref_df.iloc[idx, _loc(col)].values