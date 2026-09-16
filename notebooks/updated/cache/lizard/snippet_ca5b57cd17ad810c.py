def get_enabled(jail=None):
    ret = []
    service = _cmd(jail)
    prf = _get_jail_path(jail) if jail else ''
    for svc in __salt__['cmd.run']('{0} -e'.format(service)).splitlines():
        ret.append(os.path.basename(svc))
    for svc in get_all(jail):
        if svc in ret:
            continue
        if not os.path.exists('{0}/etc/rc.conf.d/{1}'.format(prf, svc)):
            continue
        if enabled(svc, jail=jail):
            ret.append(svc)
    return sorted(ret)