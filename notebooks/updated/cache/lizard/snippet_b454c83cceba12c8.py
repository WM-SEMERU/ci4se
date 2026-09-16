def _mod_bufsize_linux(iface, *args, **kwargs):
    ret = {'result': False, 'comment':
        'Requires rx=<val> tx==<val> rx-mini=<val> and/or rx-jumbo=<val>'}
    cmd = '/sbin/ethtool -G ' + iface
    if not kwargs:
        return ret
    if args:
        ret['comment'] = 'Unknown arguments: ' + ' '.join([six.text_type(
            item) for item in args])
        return ret
    eargs = ''
    for kw in ['rx', 'tx', 'rx-mini', 'rx-jumbo']:
        value = kwargs.get(kw)
        if value is not None:
            eargs += ' ' + kw + ' ' + six.text_type(value)
    if not eargs:
        return ret
    cmd += eargs
    out = __salt__['cmd.run'](cmd)
    if out:
        ret['comment'] = out
    else:
        ret['comment'] = eargs.strip()
        ret['result'] = True
    return ret