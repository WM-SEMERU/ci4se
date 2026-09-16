def emit(_):
    if not initialized:
        raise NotInitialized
    view = {'version': __version__, 'counters': {}, 'gauges': {},
        'histograms': {}, 'meters': {}, 'timers': {}}
    for (ty, module, name), metric in six.iteritems(all_metrics):
        view[ty]['%s.%s' % (module, name)] = metric.view()
    marshalled_view = marshal.dumps(view)
    if len(marshalled_view) > MAX_MARSHALLED_VIEW_SIZE:
        log.warn(
            'Marshalled length too large, got %d, max %d. Try recording fewer metrics or increasing MAX_MARSHALLED_VIEW_SIZE'
             % (len(marshalled_view), MAX_MARSHALLED_VIEW_SIZE))
        return
    marshalled_metrics_mmap.seek(0)
    try:
        uwsgi.lock()
        marshalled_metrics_mmap.write(marshalled_view)
    finally:
        uwsgi.unlock()