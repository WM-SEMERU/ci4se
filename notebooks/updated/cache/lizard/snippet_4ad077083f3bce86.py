def repeater(call, args=None, kwargs=None, retries=4):
    args = args or ()
    kwargs = kwargs or {}
    t = 1.0
    for x in range(retries):
        try:
            return call(*args, **kwargs)
        except APIError as ex:
            logger.error('query #%d: docker returned an error: %r', x, ex)
        except Exception as ex:
            log_last_traceback()
            logger.error('query #%d: generic error: %r', x, ex)
        t *= 2
        time.sleep(t)