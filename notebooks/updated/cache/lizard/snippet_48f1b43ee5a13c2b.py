def create_client_from_env(username=None, api_key=None, endpoint_url=None,
    timeout=None, auth=None, config_file=None, proxy=None, user_agent=None,
    transport=None, verify=True):
    settings = config.get_client_settings(username=username, api_key=
        api_key, endpoint_url=endpoint_url, timeout=timeout, proxy=proxy,
        verify=verify, config_file=config_file)
    if transport is None:
        url = settings.get('endpoint_url')
        if url is not None and '/rest' in url:
            transport = transports.RestTransport(endpoint_url=settings.get(
                'endpoint_url'), proxy=settings.get('proxy'), timeout=
                settings.get('timeout'), user_agent=user_agent, verify=verify)
        else:
            transport = transports.XmlRpcTransport(endpoint_url=settings.
                get('endpoint_url'), proxy=settings.get('proxy'), timeout=
                settings.get('timeout'), user_agent=user_agent, verify=verify)
    if auth is None and settings.get('username') and settings.get('api_key'):
        real_transport = getattr(transport, 'transport', transport)
        if isinstance(real_transport, transports.XmlRpcTransport):
            auth = slauth.BasicAuthentication(settings.get('username'),
                settings.get('api_key'))
        elif isinstance(real_transport, transports.RestTransport):
            auth = slauth.BasicHTTPAuthentication(settings.get('username'),
                settings.get('api_key'))
    return BaseClient(auth=auth, transport=transport)