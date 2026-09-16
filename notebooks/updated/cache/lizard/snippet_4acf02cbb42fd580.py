def _set_metric(self, metric_name, metric_type, value, tags=None,
    device_name=None):
    if metric_type == GAUGE:
        self.gauge(metric_name, value, tags=tags, device_name=device_name)
    elif metric_type == INCREMENT:
        self.increment(metric_name, value, tags=tags, device_name=device_name)
    else:
        self.log.error('Metric type "{}" unknown'.format(metric_type))