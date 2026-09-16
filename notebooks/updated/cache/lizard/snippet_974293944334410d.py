def get_fmri(name, **kwargs):
    if name.startswith('pkg://'):
        return name
    cmd = ['/bin/pkg', 'list', '-aHv', name]
    lines = __salt__['cmd.run_stdout'](cmd).splitlines()
    if not lines:
        return ''
    ret = []
    for line in lines:
        ret.append(_ips_get_pkgname(line))
    return ret