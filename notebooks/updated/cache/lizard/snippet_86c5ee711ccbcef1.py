def resample(df, rule, time_index, groupby=None, aggregation='mean'):
    if groupby:
        df = df.groupby(groupby)
    df = df.resample(rule, on=time_index)
    df = getattr(df, aggregation)()
    for column in groupby:
        del df[column]
    return df