def retry_on_exception(func, max_retries, exception_types, backoff_func=lambda
    n: 0):
    for i in range(0, max_retries):
        if i:
            time.sleep(backoff_func(i))
        try:
            return func()
        except exception_types as e:
            logger.debug('encountered exception on retry #{}: {!r}'.format(
                i, e))
            if i == max_retries - 1:
                raise