def _lookup_dig(name, rdtype, timeout=None, servers=None, secure=None):
    cmd = 'dig {0} -t {1} '.format(DIG_OPTIONS, rdtype)
    if servers:
        cmd += ''.join(['@{0} '.format(srv) for srv in servers])
    if timeout is not None:
        if servers:
            timeout = int(float(timeout) / len(servers))
        else:
            timeout = int(timeout)
        cmd += '+time={0} '.format(timeout)
    if secure:
        cmd += '+dnssec +adflag '
    cmd = __salt__['cmd.run_all']('{0} {1}'.format(cmd, name), python_shell
        =False, output_loglevel='quiet')
    if 'ignoring invalid type' in cmd['stderr']:
        raise ValueError('Invalid DNS type {}'.format(rdtype))
    elif cmd['retcode'] != 0:
        log.warning('dig returned (%s): %s', cmd['retcode'], cmd['stderr'].
            strip(string.whitespace + ';'))
        return False
    elif not cmd['stdout']:
        return []
    validated = False
    res = []
    for line in cmd['stdout'].splitlines():
        _, rtype, rdata = line.split(None, 2)
        if rtype == 'CNAME' and rdtype != 'CNAME':
            continue
        elif rtype == 'RRSIG':
            validated = True
            continue
        res.append(_data_clean(rdata))
    if res and secure and not validated:
        return False
    else:
        return res