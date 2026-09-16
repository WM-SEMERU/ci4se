def nPercentile(requestContext, seriesList, n):
    assert n, 'The requested percent is required to be greater than 0'
    results = []
    for s in seriesList:
        s_copy = TimeSeries(s.name, s.start, s.end, s.step, sorted(not_none(s))
            )
        if not s_copy:
            continue
        perc_val = _getPercentile(s_copy, n)
        if perc_val is not None:
            name = 'nPercentile(%s, %g)' % (s_copy.name, n)
            point_count = int((s.end - s.start) / s.step)
            perc_series = TimeSeries(name, s_copy.start, s_copy.end, s_copy
                .step, [perc_val] * point_count)
            perc_series.pathExpression = name
            results.append(perc_series)
    return results