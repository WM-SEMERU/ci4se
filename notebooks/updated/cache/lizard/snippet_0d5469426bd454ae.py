def trap_exceptions(results, handler, exceptions=Exception):
    try:
        for result in results:
            yield result
    except exceptions as exc:
        for result in always_iterable(handler(exc)):
            yield result