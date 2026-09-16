def _do_http(opts, profile='default'):
    ret = {}
    url = __salt__['config.get']('modjk:{0}:url'.format(profile), '')
    user = __salt__['config.get']('modjk:{0}:user'.format(profile), '')
    passwd = __salt__['config.get']('modjk:{0}:pass'.format(profile), '')
    realm = __salt__['config.get']('modjk:{0}:realm'.format(profile), '')
    timeout = __salt__['config.get']('modjk:{0}:timeout'.format(profile), '')
    if not url:
        raise Exception('missing url in profile {0}'.format(profile))
    if user and passwd:
        auth = _auth(url=url, realm=realm, user=user, passwd=passwd)
        _install_opener(auth)
    url += '?{0}'.format(_urlencode(opts))
    for line in _urlopen(url, timeout=timeout).read().splitlines():
        splt = line.split('=', 1)
        if splt[0] in ret:
            ret[splt[0]] += ',{0}'.format(splt[1])
        else:
            ret[splt[0]] = splt[1]
    return ret