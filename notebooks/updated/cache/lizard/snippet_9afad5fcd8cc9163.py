def repeat(obj, times=None):
    if times is None:
        return AsyncIterWrapper(sync_itertools.repeat(obj))
    return AsyncIterWrapper(sync_itertools.repeat(obj, times))