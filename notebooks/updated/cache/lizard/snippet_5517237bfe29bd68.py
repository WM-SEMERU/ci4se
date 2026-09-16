def describe_date_1d(series):
    stats = dict()
    stats['type'] = base.TYPE_DATE
    stats['min'] = series.min()
    stats['max'] = series.max()
    stats['range'] = stats['max'] - stats['min']
    stats['histogram'] = histogram(series)
    stats['mini_histogram'] = mini_histogram(series)
    return pd.Series(stats, name=series.name)