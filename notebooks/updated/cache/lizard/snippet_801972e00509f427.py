def install(name=None, refresh=False, fromrepo=None, pkgs=None, sources=
    None, **kwargs):
    try:
        pkg_params, pkg_type = __salt__['pkg_resource.parse_targets'](name,
            pkgs, sources, **kwargs)
    except MinionError as exc:
        raise CommandExecutionError(exc)
    if not pkg_params:
        return {}
    if pkg_type != 'repository':
        log.error('xbps: pkg_type "%s" not supported.', pkg_type)
        return {}
    cmd = ['xbps-install']
    if refresh:
        cmd.append('-S')
    if fromrepo:
        cmd.append('--repository={0}'.format(fromrepo))
    cmd.append('-y')
    cmd.extend(pkg_params)
    old = list_pkgs()
    __salt__['cmd.run'](cmd, output_loglevel='trace')
    __context__.pop('pkg.list_pkgs', None)
    new = list_pkgs()
    _rehash()
    return salt.utils.data.compare_dicts(old, new)