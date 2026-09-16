def dfsyn2appended(df, colsyn, colsynfmt=None, colsynstrsep=';'):
    colsynappended = colsyn + ' appended'
    df.index = range(len(df))
    if colsynfmt == 'str':
        df.loc[:, (colsyn)] = df.loc[:, (colsyn)].apply(lambda x: x.split(
            colsynstrsep))
    dfsynappended = df[colsyn].apply(pd.Series).unstack().reset_index().drop(
        'level_0', axis=1).set_index('level_1')
    dfsynappended.columns = [colsynappended]
    dfsynappended = dfsynappended.dropna()
    return dfsynappended.join(df, how='left')