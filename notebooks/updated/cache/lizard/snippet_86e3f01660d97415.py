def regular_index(*dfs):
    original_index = [df.index for df in dfs]
    have_bad_index = [(not isinstance(df.index, pd.RangeIndex)) for df in dfs]
    for df, bad in zip(dfs, have_bad_index):
        if bad:
            df.reset_index(drop=True, inplace=True)
    try:
        yield dfs
    finally:
        for df, bad, idx in zip(dfs, have_bad_index, original_index):
            if bad and len(df.index) == len(idx):
                df.index = idx