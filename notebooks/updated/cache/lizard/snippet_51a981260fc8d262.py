def describe_supported(series, **kwargs):
    leng = len(series)
    count = series.count()
    n_infinite = count - series.count()
    value_counts, distinct_count = base.get_groupby_statistic(series)
    if count > distinct_count > 1:
        mode = series.mode().iloc[0]
    else:
        mode = series[0]
    results_data = {'count': count, 'distinct_count': distinct_count,
        'p_missing': 1 - count * 1.0 / leng, 'n_missing': leng - count,
        'p_infinite': n_infinite * 1.0 / leng, 'n_infinite': n_infinite,
        'is_unique': distinct_count == leng, 'mode': mode, 'p_unique': 
        distinct_count * 1.0 / leng}
    try:
        results_data['memorysize'] = series.memory_usage()
    except:
        results_data['memorysize'] = 0
    return pd.Series(results_data, name=series.name)