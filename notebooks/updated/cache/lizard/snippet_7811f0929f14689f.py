def _measurements(session_group, metric_name):
    for session_index, session in enumerate(session_group.sessions):
        metric_value = _find_metric_value(session, metric_name)
        if not metric_value:
            continue
        yield _Measurement(metric_value, session_index)