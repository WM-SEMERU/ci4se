def enable(name, **kwargs):
    if 'runlevels' in kwargs:
        requested_levels = set(kwargs['runlevels'] if isinstance(kwargs[
            'runlevels'], list) else [kwargs['runlevels']])
        enabled_levels, disabled_levels = _enable_delta(name, requested_levels)
        commands = []
        if disabled_levels:
            commands.append(_enable_disable_cmd(name, 'delete',
                disabled_levels))
        if enabled_levels:
            commands.append(_enable_disable_cmd(name, 'add', enabled_levels))
        if not commands:
            return True
    else:
        commands = [_enable_disable_cmd(name, 'add')]
    for cmd in commands:
        if _ret_code(cmd):
            return False
    return True