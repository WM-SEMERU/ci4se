def _netstat_sunos():
    log.warning('User and program not (yet) supported on SunOS')
    ret = []
    for addr_family in ('inet', 'inet6'):
        cmd = 'netstat -f {0} -P tcp -an | tail +5'.format(addr_family)
        out = __salt__['cmd.run'](cmd, python_shell=True)
        for line in out.splitlines():
            comps = line.split()
            ret.append({'proto': 'tcp6' if addr_family == 'inet6' else
                'tcp', 'recv-q': comps[5], 'send-q': comps[4],
                'local-address': comps[0], 'remote-address': comps[1],
                'state': comps[6]})
        cmd = 'netstat -f {0} -P udp -an | tail +5'.format(addr_family)
        out = __salt__['cmd.run'](cmd, python_shell=True)
        for line in out.splitlines():
            comps = line.split()
            ret.append({'proto': 'udp6' if addr_family == 'inet6' else
                'udp', 'local-address': comps[0], 'remote-address': comps[1
                ] if len(comps) > 2 else ''})
    return ret