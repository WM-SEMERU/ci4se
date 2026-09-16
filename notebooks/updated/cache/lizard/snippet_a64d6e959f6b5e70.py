def bulk_disable(workers, lbn, profile='default'):
    ret = {}
    if isinstance(workers, six.string_types):
        workers = workers.split(',')
    for worker in workers:
        try:
            ret[worker] = worker_disable(worker, lbn, profile)
        except Exception:
            ret[worker] = False
    return ret