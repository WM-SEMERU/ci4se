def remove(name=None, pkgs=None, **kwargs):
    targets = salt.utils.args.split_input(pkgs) if pkgs else [name]
    if not targets:
        return {}
    if pkgs:
        log.debug('Removing these fileset(s)/rpm package(s) %s: %s', name,
            targets)
    errors = []
    old = list_pkgs()
    for target in targets:
        try:
            named, versionpkg, rpmpkg = _check_pkg(target)
        except CommandExecutionError as exc:
            if exc.info:
                errors.append(exc.info['errors'])
            continue
        if rpmpkg:
            cmd = ['/usr/bin/rpm', '-e', named]
            out = __salt__['cmd.run_all'](cmd, output_loglevel='trace')
        else:
            cmd = ['/usr/sbin/installp', '-u', named]
            out = __salt__['cmd.run_all'](cmd, output_loglevel='trace')
    __context__.pop('pkg.list_pkgs', None)
    new = list_pkgs()
    ret = salt.utils.data.compare_dicts(old, new)
    if errors:
        raise CommandExecutionError(
            'Problems encountered removing filesets(s)/package(s)', info={
            'changes': ret, 'errors': errors})
    return ret