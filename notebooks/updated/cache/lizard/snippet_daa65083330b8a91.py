def active(extended=False):
    ret = {}
    if __grains__['os'] == 'FreeBSD':
        _active_mounts_freebsd(ret)
    elif 'AIX' in __grains__['kernel']:
        _active_mounts_aix(ret)
    elif __grains__['kernel'] == 'SunOS':
        _active_mounts_solaris(ret)
    elif __grains__['os'] == 'OpenBSD':
        _active_mounts_openbsd(ret)
    elif __grains__['os'] in ['MacOS', 'Darwin']:
        _active_mounts_darwin(ret)
    elif extended:
        try:
            _active_mountinfo(ret)
        except CommandExecutionError:
            _active_mounts(ret)
    else:
        _active_mounts(ret)
    return ret