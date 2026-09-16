def _main_ctxmgr(func):

    @functools.wraps(func)
    def helper(*args, **kwargs):
        return ServerMainContextManager(func, args, kwargs)
    return helper