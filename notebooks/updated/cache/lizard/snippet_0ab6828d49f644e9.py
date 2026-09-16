def validate_uuid_representation(dummy, value):
    try:
        return _UUID_REPRESENTATIONS[value]
    except KeyError:
        raise ValueError(
            '%s is an invalid UUID representation. Must be one of %s' % (
            value, tuple(_UUID_REPRESENTATIONS)))