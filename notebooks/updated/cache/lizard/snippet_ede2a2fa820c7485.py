def multifile_dataframe(paths=['urbanslang{}of4.csv'.format(i) for i in
    range(1, 5)], header=0, index_col=None):
    df = pd.DataFrame()
    for p in paths:
        df = df.append(read_csv(p, header=header, index_col=index_col),
            ignore_index=True if not index_col else False)
    if index_col and df.index.name == index_col:
        del df[index_col]
    return df