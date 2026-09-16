def _netinfo_freebsd_netbsd():
    ret = {}
    out = __salt__['cmd.run']('sockstat -46 {0} | tail -n+2'.format('-n' if
        __grains__['kernel'] == 'NetBSD' else ''), python_shell=True)
    for line in out.splitlines():
        user, cmd, pid, _, proto, local_addr, remote_addr = line.split()
        local_addr = '.'.join(local_addr.rsplit(':', 1))
        remote_addr = '.'.join(remote_addr.rsplit(':', 1))
        ret.setdefault(local_addr, {}).setdefault(remote_addr, {}).setdefault(
            proto, {}).setdefault(pid, {})['user'] = user
        ret[local_addr][remote_addr][proto][pid]['cmd'] = cmd
    return ret