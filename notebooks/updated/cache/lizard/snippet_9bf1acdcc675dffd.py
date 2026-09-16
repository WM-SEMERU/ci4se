def handle_connection_repl(client):
    client.settimeout(None)
    backup = []
    old_interval = getinterval()
    patches = [('r', ('stdin', '__stdin__')), ('w', ('stdout', '__stdout__'))]
    if _MANHOLE.redirect_stderr:
        patches.append(('w', ('stderr', '__stderr__')))
    try:
        client_fd = client.fileno()
        for mode, names in patches:
            for name in names:
                backup.append((name, getattr(sys, name)))
                setattr(sys, name, _ORIGINAL_FDOPEN(client_fd, mode, 1 if
                    PY3 else 0))
        try:
            handle_repl(_MANHOLE.locals)
        except Exception as exc:
            _LOG('REPL failed with %r.' % exc)
        _LOG('DONE.')
    finally:
        try:
            setinterval(2147483647)
            try:
                client.close()
            except IOError:
                pass
            junk = []
            for name, fh in backup:
                junk.append(getattr(sys, name))
                setattr(sys, name, fh)
            del backup
            for fh in junk:
                try:
                    if hasattr(fh, 'detach'):
                        fh.detach()
                    else:
                        fh.close()
                except IOError:
                    pass
                del fh
            del junk
        finally:
            setinterval(old_interval)
            _LOG('Cleaned up.')