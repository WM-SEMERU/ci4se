def retry(delays=(0, 1, 1, 4, 16, 64), timeout=300, predicate=never):
    if timeout > 0:
        go = [None]

        @contextmanager
        def repeated_attempt(delay):
            try:
                yield
            except Exception as e:
                if time.time() + delay < expiration and predicate(e):
                    log.info('Got %s, trying again in %is.', e, delay)
                    time.sleep(delay)
                else:
                    raise
            else:
                go.pop()
        delays = iter(delays)
        expiration = time.time() + timeout
        delay = next(delays)
        while go:
            yield repeated_attempt(delay)
            delay = next(delays, delay)
    else:

        @contextmanager
        def single_attempt():
            yield
        yield single_attempt()