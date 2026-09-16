def auth_token(registry, repo):
    auth_info = auth_config.resolve_authconfig(registry)
    if auth_info:
        normalized = {k.lower(): v for k, v in six.iteritems(auth_info)}
        auth_info = normalized.get('username'), normalized.get('password')
    response = requests.get('https://{}/v2/'.format(registry), timeout=3)
    if response.headers.get('www-authenticate'):
        try:
            info = www_authenticate.parse(response.headers['www-authenticate'])
        except ValueError:
            info = {}
    else:
        log.error('Received {} when attempting to authenticate with {}'.
            format(response, registry))
        info = {}
    if info.get('bearer'):
        res = requests.get(info['bearer']['realm'] +
            '?service={}&scope=repository:{}:pull'.format(info['bearer'][
            'service'], repo), auth=auth_info, timeout=3)
        res.raise_for_status()
        return res.json()
    return {}