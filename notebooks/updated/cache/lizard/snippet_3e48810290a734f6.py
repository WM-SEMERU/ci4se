def get_default_gateway():
    try:
        return next(iter(x.split()[-1] for x in __salt__['cmd.run']([
            'netsh', 'interface', 'ip', 'show', 'config'], python_shell=
            False).splitlines() if 'Default Gateway:' in x))
    except StopIteration:
        raise CommandExecutionError('Unable to find default gateway')