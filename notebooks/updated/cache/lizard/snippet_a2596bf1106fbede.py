def str_traceback(error, tb):
    if not isinstance(tb, types.TracebackType):
        return tb
    return ''.join(traceback.format_exception(error.__class__, error, tb))