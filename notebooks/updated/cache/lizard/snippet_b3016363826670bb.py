def construct(key_data, algorithm=None):
    if not algorithm and isinstance(key_data, dict):
        algorithm = key_data.get('alg', None)
    if not algorithm:
        raise JWKError('Unable to find a algorithm for key: %s' % key_data)
    key_class = get_key(algorithm)
    if not key_class:
        raise JWKError('Unable to find a algorithm for key: %s' % key_data)
    return key_class(key_data, algorithm)