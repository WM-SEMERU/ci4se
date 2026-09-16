def worker_edit(worker, lbn, settings, profile='default'):
    settings['cmd'] = 'update'
    settings['mime'] = 'prop'
    settings['w'] = lbn
    settings['sw'] = worker
    return _do_http(settings, profile)['worker.result.type'] == 'OK'