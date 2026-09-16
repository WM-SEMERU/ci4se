def series(*coros_or_futures, timeout=None, loop=None, return_exceptions=False
    ):
    return (yield from gather(*coros_or_futures, loop=loop, limit=1,
        timeout=timeout, return_exceptions=return_exceptions))