def install_twisted():
    global emit, _call_partial
    try:
        from twisted.internet import defer
        emit = _emit_twisted
        _call_partial = defer.maybeDeferred
        return True
    except ImportError:
        _call_partial = lambda fn, *a, **kw: fn(*a, **kw)
        return False