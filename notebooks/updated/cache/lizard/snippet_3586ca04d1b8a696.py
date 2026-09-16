def remove(name=None, pkgs=None, saltenv='base', **kwargs):
    try:
        pkg_params = __salt__['pkg_resource.parse_targets'](name, pkgs)[0]
    except MinionError as exc:
        raise CommandExecutionError(exc)
    old = list_pkgs()
    targets = [x for x in pkg_params if x in old]
    if not targets:
        return {}
    try:
        if 'admin_source' in kwargs:
            adminfile = __salt__['cp.cache_file'](kwargs['admin_source'],
                saltenv)
        else:
            adminfile = _write_adminfile(kwargs)
        cmd = ['/usr/sbin/pkgrm', '-n', '-a', adminfile] + targets
        out = __salt__['cmd.run_all'](cmd, python_shell=False,
            output_loglevel='trace')
        if out['retcode'] != 0 and out['stderr']:
            errors = [out['stderr']]
        else:
            errors = []
        __context__.pop('pkg.list_pkgs', None)
        new = list_pkgs()
        ret = salt.utils.data.compare_dicts(old, new)
        if errors:
            raise CommandExecutionError(
                'Problem encountered removing package(s)', info={'errors':
                errors, 'changes': ret})
    finally:
        if 'admin_source' not in kwargs:
            try:
                os.remove(adminfile)
            except (NameError, OSError):
                pass
    return ret