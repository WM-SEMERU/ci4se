def assert_is_valid_key(key):
    if SETTINGS.CONFIG.ENFORCE_KEYS_MONGO_COMPATIBLE and (isinstance(key,
        basestring) and ('.' in key or key[0] == '$')):
        raise KeyError(
            'Invalid key "{}". Config-keys cannot contain "." or start with "$"'
            .format(key))
    if SETTINGS.CONFIG.ENFORCE_KEYS_JSONPICKLE_COMPATIBLE and isinstance(key,
        basestring) and (key in jsonpickle.tags.RESERVED or key.startswith(
        'json://')):
        raise KeyError(
            'Invalid key "{}". Config-keys cannot be one of thereserved jsonpickle tags: {}'
            .format(key, jsonpickle.tags.RESERVED))
    if SETTINGS.CONFIG.ENFORCE_STRING_KEYS and not isinstance(key, basestring):
        raise KeyError(
            'Invalid key "{}". Config-keys have to be strings, but was {}'.
            format(key, type(key)))
    if SETTINGS.CONFIG.ENFORCE_VALID_PYTHON_IDENTIFIER_KEYS and (isinstance
        (key, basestring) and not PYTHON_IDENTIFIER.match(key)):
        raise KeyError('Key "{}" is not a valid python identifier'.format(key))
    if SETTINGS.CONFIG.ENFORCE_KEYS_NO_EQUALS and (isinstance(key,
        basestring) and '=' in key):
        raise KeyError(
            'Invalid key "{}". Config keys may not contain anequals sign ("=").'
            .format('='))