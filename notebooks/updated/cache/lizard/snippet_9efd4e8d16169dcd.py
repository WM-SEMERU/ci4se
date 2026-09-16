def from_client(cls, client):
    if hasattr(client, 'client_configuration'):
        return client.client_configuration
    kwargs = {'client': client}
    for attr in cls.init_kwargs:
        if hasattr(client, attr):
            kwargs[attr] = getattr(client, attr)
    if hasattr(client, 'api_version'):
        kwargs['version'] = client.api_version
    return cls(**kwargs)