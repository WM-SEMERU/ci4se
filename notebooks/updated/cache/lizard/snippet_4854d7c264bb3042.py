def filter_traceback(error, tb, ignore_pkg=CURRENT_PACKAGE):
    if not isinstance(tb, types.TracebackType):
        return tb

    def in_namespace(n):
        return n and (n.startswith(ignore_pkg + '.') or n == ignore_pkg)
    while tb and in_namespace(tb.tb_frame.f_globals['__package__']):
        tb = tb.tb_next
    starting_tb = tb
    limit = 0
    while tb and not in_namespace(tb.tb_frame.f_globals['__package__']):
        tb = tb.tb_next
        limit += 1
    return ''.join(traceback.format_exception(error.__class__, error,
        starting_tb, limit))