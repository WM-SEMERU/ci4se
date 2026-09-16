def get_settings_from_client(client):
    settings = {'username': '', 'api_key': '', 'timeout': '',
        'endpoint_url': ''}
    try:
        settings['username'] = client.auth.username
        settings['api_key'] = client.auth.api_key
    except AttributeError:
        pass
    transport = _resolve_transport(client.transport)
    try:
        settings['timeout'] = transport.timeout
        settings['endpoint_url'] = transport.endpoint_url
    except AttributeError:
        pass
    return settings