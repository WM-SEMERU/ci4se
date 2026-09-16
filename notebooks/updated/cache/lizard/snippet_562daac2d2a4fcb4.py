def _stamp_and_update_hook(method, dependencies, stampfile, func, *args, **
    kwargs):
    result = _stamp(stampfile, func, *args, **kwargs)
    method.update_stampfile_hook(dependencies)
    return result