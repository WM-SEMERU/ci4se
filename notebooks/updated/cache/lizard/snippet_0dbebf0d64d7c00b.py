def unfreeze(name, path=None, use_vt=None):
    _ensure_exists(name, path=path)
    if state(name, path=path) == 'stopped':
        raise CommandExecutionError("Container '{0}' is stopped".format(name))
    cmd = 'lxc-unfreeze'
    if path:
        cmd += ' -P {0}'.format(pipes.quote(path))
    return _change_state(cmd, name, 'running', path=path, use_vt=use_vt)