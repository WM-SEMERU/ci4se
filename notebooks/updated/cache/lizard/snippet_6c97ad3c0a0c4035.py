def nelson_aalen_estimator(event, time):
    event, time = check_y_survival(event, time)
    check_consistent_length(event, time)
    uniq_times, n_events, n_at_risk = _compute_counts(event, time)
    y = numpy.cumsum(n_events / n_at_risk)
    return uniq_times, y