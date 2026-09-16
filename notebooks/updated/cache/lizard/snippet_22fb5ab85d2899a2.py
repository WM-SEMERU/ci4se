def add_repo_key(path=None, text=None, keyserver=None, keyid=None, saltenv=
    'base'):
    cmd = ['apt-key']
    kwargs = {}
    current_repo_keys = get_repo_keys()
    if path:
        cached_source_path = __salt__['cp.cache_file'](path, saltenv)
        if not cached_source_path:
            log.error('Unable to get cached copy of file: %s', path)
            return False
        cmd.extend(['add', cached_source_path])
    elif text:
        log.debug('Received value: %s', text)
        cmd.extend(['add', '-'])
        kwargs.update({'stdin': text})
    elif keyserver:
        if not keyid:
            error_msg = ('No keyid or keyid too short for keyserver: {0}'.
                format(keyserver))
            raise SaltInvocationError(error_msg)
        cmd.extend(['adv', '--batch', '--keyserver', keyserver, '--recv',
            keyid])
    elif keyid:
        error_msg = 'No keyserver specified for keyid: {0}'.format(keyid)
        raise SaltInvocationError(error_msg)
    else:
        raise TypeError('{0}() takes at least 1 argument (0 given)'.format(
            add_repo_key.__name__))
    if keyid:
        for current_keyid in current_repo_keys:
            if current_keyid[-len(keyid):] == keyid:
                log.debug("The keyid '%s' already present: %s", keyid,
                    current_keyid)
                return True
    cmd_ret = _call_apt(cmd, **kwargs)
    if cmd_ret['retcode'] == 0:
        return True
    log.error('Unable to add repo key: %s', cmd_ret['stderr'])
    return False