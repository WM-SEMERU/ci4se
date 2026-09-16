def drop_duplicates_agg(df, colsgroupby, cols2aggf, test=False):
    if test:
        print(df.shape)
        print(df.drop_duplicates(subset=colsgroupby).shape)
    dfdupagg = df.loc[(df.duplicated(subset=colsgroupby, keep=False)), :
        ].groupby(colsgroupby).agg(cols2aggf)
    df_ = df.drop_duplicates(subset=colsgroupby, keep=False)
    if test:
        print(df_.shape)
    dfout = df_.append(dfdupagg, sort=True)
    if test:
        print(dfout.shape)
    return dfout