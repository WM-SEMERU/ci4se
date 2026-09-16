def metric_crud(client, to_delete):
    METRIC_NAME = 'robots-%d' % (_millis(),)
    DESCRIPTION = 'Robots all up in your server'
    FILTER = 'logName:apache-access AND textPayload:robot'
    UPDATED_FILTER = 'textPayload:robot'
    UPDATED_DESCRIPTION = 'Danger, Will Robinson!'
    for metric in client.list_metrics():
        do_something_with(metric)
    metric = client.metric(METRIC_NAME, filter_=FILTER, description=DESCRIPTION
        )
    assert not metric.exists()
    metric.create()
    assert metric.exists()
    to_delete.append(metric)
    existing_metric = client.metric(METRIC_NAME)
    existing_metric.reload()
    assert existing_metric.filter_ == FILTER
    assert existing_metric.description == DESCRIPTION
    existing_metric.filter_ = UPDATED_FILTER
    existing_metric.description = UPDATED_DESCRIPTION
    existing_metric.update()
    existing_metric.reload()
    assert existing_metric.filter_ == UPDATED_FILTER
    assert existing_metric.description == UPDATED_DESCRIPTION

    def _metric_delete():
        metric.delete()
    _backoff_not_found(_metric_delete)
    to_delete.remove(metric)