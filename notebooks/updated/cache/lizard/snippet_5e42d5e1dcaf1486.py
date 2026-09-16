def _session(kwargs):
    if 'session' in kwargs:
        LOG.debug('Reusing session')
        sess = kwargs.get('session')
        if not isinstance(sess, k_session.Session):
            msg = 'session should be an instance of %s' % k_session.Session
            LOG.error(msg)
            raise RuntimeError(msg)
    else:
        LOG.debug('Initializing new session')
        auth = _get_auth_handler(kwargs)
        sess = _get_session(auth, kwargs)
    return sess