def volume_attach(provider, names, **kwargs):
    client = _get_client()
    info = client.extra_action(provider=provider, names=names, action=
        'volume_attach', **kwargs)
    return info