def retry(tries=10, delay=1, backoff=2, retry_exception=None):
    assert tries > 0, 'tries must be 1 or greater'
    catching_mode = bool(retry_exception)

    def deco_retry(f):

        @functools.wraps(f)
        def f_retry(*args, **kwargs):
            mtries, mdelay = tries, delay
            while mtries > 0:
                time.sleep(mdelay)
                mdelay *= backoff
                try:
                    rv = f(*args, **kwargs)
                    if not catching_mode and rv:
                        return rv
                except retry_exception:
                    pass
                else:
                    if catching_mode:
                        return rv
                mtries -= 1
                if mtries is 0 and not catching_mode:
                    return False
                if mtries is 0 and catching_mode:
                    return f(*args, **kwargs)
                log.debug('{0} try, sleeping for {1} sec'.format(tries -
                    mtries, mdelay))
            raise Exception('unreachable code')
        return f_retry
    return deco_retry