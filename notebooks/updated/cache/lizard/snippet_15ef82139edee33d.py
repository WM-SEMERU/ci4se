def _walk(path, value, metrics, timestamp, skip):
    log.trace(
        'Carbon return walking path: %s, value: %s, metrics: %s, timestamp: %s'
        , path, value, metrics, timestamp)
    if isinstance(value, collections.Mapping):
        for key, val in six.iteritems(value):
            _walk('{0}.{1}'.format(path, key), val, metrics, timestamp, skip)
    elif isinstance(value, list):
        for item in value:
            _walk('{0}.{1}'.format(path, item), item, metrics, timestamp, skip)
    else:
        try:
            val = float(value)
            metrics.append((path, val, timestamp))
        except (TypeError, ValueError):
            msg = (
                'Error in carbon returner, when trying to convert metric: {0}, with val: {1}'
                .format(path, value))
            if skip:
                log.debug(msg)
            else:
                log.info(msg)
                raise