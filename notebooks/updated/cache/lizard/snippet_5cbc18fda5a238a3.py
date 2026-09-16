def ipv6(value, allow_empty=False, **kwargs):
    if not value and allow_empty is False:
        raise errors.EmptyValueError('value (%s) was empty' % value)
    elif not value:
        return None
    if not isinstance(value, str):
        raise errors.InvalidIPAddressError('value (%s) is not a valid ipv6' %
            value)
    value = value.lower().strip()
    is_valid = IPV6_REGEX.match(value)
    if not is_valid:
        raise errors.InvalidIPAddressError('value (%s) is not a valid ipv6' %
            value)
    return value