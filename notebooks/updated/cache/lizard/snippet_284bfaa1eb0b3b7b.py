def wrap_connection_loader__get(name, *args, **kwargs):
    if name in ('docker', 'kubectl', 'jail', 'local', 'lxc', 'lxd',
        'machinectl', 'setns', 'ssh'):
        name = 'mitogen_' + name
    return connection_loader__get(name, *args, **kwargs)