def get_hostname(cls, container_name, client_name=None):
    base_name = container_name
    for old, new in cls.hostname_replace:
        base_name = base_name.replace(old, new)
    if not client_name or client_name == cls.default_client_name:
        return base_name
    client_suffix = client_name
    for old, new in cls.hostname_replace:
        client_suffix = client_suffix.replace(old, new)
    return '{0}-{1}'.format(base_name, client_suffix)