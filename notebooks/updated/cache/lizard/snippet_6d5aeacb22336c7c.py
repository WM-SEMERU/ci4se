def traceroute(host):
    ret = []
    cmd = ['tracert', salt.utils.network.sanitize_host(host)]
    lines = __salt__['cmd.run'](cmd, python_shell=False).splitlines()
    for line in lines:
        if ' ' not in line:
            continue
        if line.startswith('Trac'):
            continue
        if line.startswith('over'):
            continue
        comps = line.split()
        complength = len(comps)
        if complength == 9:
            result = {'count': comps[0], 'hostname': comps[7], 'ip': comps[
                8], 'ms1': comps[1], 'ms2': comps[3], 'ms3': comps[5]}
            ret.append(result)
        elif complength == 8:
            result = {'count': comps[0], 'hostname': None, 'ip': comps[7],
                'ms1': comps[1], 'ms2': comps[3], 'ms3': comps[5]}
            ret.append(result)
        else:
            result = {'count': comps[0], 'hostname': None, 'ip': None,
                'ms1': None, 'ms2': None, 'ms3': None}
            ret.append(result)
    return ret