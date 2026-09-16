def run_tag_from_session_and_metric(session_name, metric_name):
    assert isinstance(session_name, six.string_types)
    assert isinstance(metric_name, api_pb2.MetricName)
    run = os.path.normpath(os.path.join(session_name, metric_name.group))
    tag = metric_name.tag
    return run, tag