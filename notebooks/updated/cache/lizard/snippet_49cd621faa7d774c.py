def df2list(df):
    subjects = df.index.levels[0].values.tolist()
    lists = df.index.levels[1].values.tolist()
    idx = pd.IndexSlice
    df = df.loc[idx[subjects, lists], df.columns]
    lst = [df.loc[(sub), :].values.tolist() for sub in subjects]
    return lst