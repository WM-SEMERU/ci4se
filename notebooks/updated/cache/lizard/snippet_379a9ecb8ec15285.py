def _call_yum(args, **kwargs):
    params = {'output_loglevel': 'trace', 'python_shell': False, 'env':
        salt.utils.environment.get_module_environment(globals())}
    params.update(kwargs)
    cmd = []
    if salt.utils.systemd.has_scope(__context__) and __salt__['config.get'](
        'systemd.scope', True):
        cmd.extend(['systemd-run', '--scope'])
    cmd.append(_yum())
    cmd.extend(args)
    return __salt__['cmd.run_all'](cmd, **params)