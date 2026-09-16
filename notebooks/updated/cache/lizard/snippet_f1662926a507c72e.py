def unwatch(value):
    if not isinstance(value, Watchable):
        raise TypeError('Expected a Watchable, not %r.' % value)
    spectator = watcher(value)
    try:
        del value._instance_spectator
    except Exception:
        pass
    return spectator