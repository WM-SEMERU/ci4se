def is_valid_endpoint(endpoint):
    try:
        if urlsplit(endpoint).scheme:
            raise InvalidEndpointError('Hostname cannot have a scheme.')
        hostname = endpoint.split(':')[0]
        if hostname is None:
            raise InvalidEndpointError('Hostname cannot be empty.')
        if len(hostname) > 255:
            raise InvalidEndpointError('Hostname cannot be greater than 255.')
        if hostname[-1] == '.':
            hostname = hostname[:-1]
        if not _ALLOWED_HOSTNAME_REGEX.match(hostname):
            raise InvalidEndpointError('Hostname does not meet URL standards.')
    except AttributeError as error:
        raise TypeError(error)
    return True