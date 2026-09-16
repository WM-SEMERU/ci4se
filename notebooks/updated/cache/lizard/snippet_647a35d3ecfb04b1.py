def _wget(cmd, opts=None, url='http://localhost:8080/manager', timeout=180):
    ret = {'res': True, 'msg': []}
    auth = _auth(url)
    if auth is False:
        ret['res'] = False
        ret['msg'] = 'missing username and password settings (grain/pillar)'
        return ret
    if url[-1] != '/':
        url += '/'
    url6 = url
    url += 'text/{0}'.format(cmd)
    url6 += '{0}'.format(cmd)
    if opts:
        url += '?{0}'.format(_urlencode(opts))
        url6 += '?{0}'.format(_urlencode(opts))
    _install_opener(auth)
    try:
        ret['msg'] = _urlopen(url, timeout=timeout).read().splitlines()
    except Exception:
        try:
            ret['msg'] = _urlopen(url6, timeout=timeout).read().splitlines()
        except Exception:
            ret['msg'] = 'Failed to create HTTP request'
    if not ret['msg'][0].startswith('OK'):
        ret['res'] = False
    return ret