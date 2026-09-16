def current(cls):
    try:
        return _tls.loop
    except AttributeError:
        if threading.current_thread().name == 'MainThread':
            _tls.loop = cls()
            return _tls.loop
        raise RuntimeError(
            'there is no event loop created in the current thread')