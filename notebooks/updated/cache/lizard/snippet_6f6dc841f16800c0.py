def _query_wrap(fun, *args, **kwargs):
    with _query_lock:
        global _last_query_time
        since_last_query = time.time() - _last_query_time
        if since_last_query < QUERY_WAIT_TIME:
            time.sleep(QUERY_WAIT_TIME - since_last_query)
        _last_query_time = time.time()
        return fun(*args, **kwargs)