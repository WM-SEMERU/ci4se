def worker_activated(name, workers=None, profile='default'):
    if workers is None:
        workers = []
    return _bulk_state('modjk.bulk_activate', name, workers, profile)