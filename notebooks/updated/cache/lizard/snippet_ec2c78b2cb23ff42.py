def _process_metric(self, data, metric, xtype, path, xform=None, tags=None,
    hostname=None):
    value = data
    for key in path.split('.'):
        if value is not None:
            value = value.get(key)
        else:
            break
    if value is not None:
        if xform:
            value = xform(value)
        if xtype == 'gauge':
            self.gauge(metric, value, tags=tags, hostname=hostname)
        else:
            self.rate(metric, value, tags=tags, hostname=hostname)
    else:
        self.log.debug('Metric not found: %s -> %s', path, metric)