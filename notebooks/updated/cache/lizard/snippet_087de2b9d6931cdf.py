def describe_handler(h):
    t = h.__class__
    format = handler_formats.get(t)
    if format is not None:
        yield format % h.__dict__
    else:
        yield repr(h)
    level = getattr(h, 'level', logging.NOTSET)
    if level != logging.NOTSET:
        yield '  Level ' + logging.getLevelName(level)
    for f in getattr(h, 'filters', ()):
        yield '  Filter %s' % describe_filter(f)
    formatter = getattr(h, 'formatter', None)
    if formatter is not None:
        if type(formatter) is logging.Formatter:
            yield '  Formatter fmt=%r datefmt=%r' % (getattr(formatter,
                '_fmt', None), getattr(formatter, 'datefmt', None))
        else:
            yield '  Formatter %r' % (formatter,)
    if t is logging.handlers.MemoryHandler and h.target is not None:
        yield '  Flushes output to:'
        g = describe_handler(h.target)
        yield '    Handler ' + next(g)
        for line in g:
            yield '    ' + line