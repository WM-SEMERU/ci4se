def _set_extremum_session_metrics(session_group, aggregation_metric,
    extremum_fn):
    measurements = _measurements(session_group, aggregation_metric)
    ext_session = extremum_fn(measurements, key=operator.attrgetter(
        'metric_value.value')).session_index
    del session_group.metric_values[:]
    session_group.metric_values.MergeFrom(session_group.sessions[
        ext_session].metric_values)