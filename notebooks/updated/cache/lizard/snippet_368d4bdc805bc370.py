def discover(email, credentials):
    log.debug('Attempting autodiscover on email %s', email)
    if not isinstance(credentials, Credentials):
        raise ValueError("'credentials' %r must be a Credentials instance" %
            credentials)
    domain = get_domain(email)
    autodiscover_key = domain, credentials
    log.debug('Waiting for _autodiscover_cache_lock')
    with _autodiscover_cache_lock:
        log.debug('_autodiscover_cache_lock acquired')
        if autodiscover_key in _autodiscover_cache:
            protocol = _autodiscover_cache[autodiscover_key]
            if not isinstance(protocol, AutodiscoverProtocol):
                raise ValueError(
                    'Unexpected autodiscover cache contents: %s' % protocol)
            log.debug('Cache hit for domain %s credentials %s: %s', domain,
                credentials, protocol.server)
            try:
                return _autodiscover_quick(credentials=credentials, email=
                    email, protocol=protocol)
            except AutoDiscoverFailed:
                del _autodiscover_cache[autodiscover_key]
            except AutoDiscoverRedirect as e:
                log.debug('%s redirects to %s', email, e.redirect_email)
                if email.lower() == e.redirect_email.lower():
                    raise_from(AutoDiscoverCircularRedirect(
                        'Redirect to same email address: %s' % email), None)
                email = e.redirect_email
        else:
            log.debug('Cache miss for domain %s credentials %s', domain,
                credentials)
            log.debug('Cache contents: %s', _autodiscover_cache)
            try:
                return _try_autodiscover(hostname=domain, credentials=
                    credentials, email=email)
            except AutoDiscoverRedirect as e:
                if email.lower() == e.redirect_email.lower():
                    raise_from(AutoDiscoverCircularRedirect(
                        'Redirect to same email address: %s' % email), None)
                log.debug('%s redirects to %s', email, e.redirect_email)
                email = e.redirect_email
    log.debug('Released autodiscover_cache_lock')
    return discover(email=email, credentials=credentials)