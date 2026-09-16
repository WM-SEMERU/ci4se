def list_pkgs(versions_as_list=False, **kwargs):
    ret = {}
    versions_as_list = salt.utils.data.is_true(versions_as_list)
    if any([salt.utils.data.is_true(kwargs.get(x)) for x in ('removed',
        'purge_desired')]):
        return ret
    if 'pkg.list_pkgs' in __context__:
        if versions_as_list:
            return __context__['pkg.list_pkgs']
        else:
            ret = copy.deepcopy(__context__['pkg.list_pkgs'])
            __salt__['pkg_resource.stringify'](ret)
            return ret
    cmd = '/usr/bin/lslpp -Lc'
    lines = __salt__['cmd.run'](cmd, python_shell=False).splitlines()
    for line in lines:
        if line.startswith('#'):
            continue
        comps = line.split(':')
        if len(comps) < 7:
            continue
        if 'R' in comps[6]:
            name = comps[0]
        else:
            name = comps[1]
        version_num = comps[2]
        __salt__['pkg_resource.add_pkg'](ret, name, version_num)
    __salt__['pkg_resource.sort_pkglist'](ret)
    __context__['pkg.list_pkgs'] = copy.deepcopy(ret)
    if not versions_as_list:
        __salt__['pkg_resource.stringify'](ret)
    return ret