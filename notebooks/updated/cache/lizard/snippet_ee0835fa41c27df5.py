def get_type_item(self, value):
    if isinstance(value, (UsedVolume, SharedVolume)):
        if value.readonly:
            raise ValueError('Attached volumes should not be read-only.')
        return value
    elif isinstance(value, six.string_types):
        return SharedVolume(value)
    elif isinstance(value, (list, tuple)):
        v_len = len(value)
        if v_len == 2:
            if value[1]:
                return UsedVolume(value[0], value[1])
            return SharedVolume(value[0])
        elif v_len == 1:
            return SharedVolume(value[0])
        raise ValueError(
            'Invalid element length; only tuples and lists of length 1-2 can be converted to a UsedVolume or SharedVolume tuple; found length {0}.'
            .format(v_len))
    elif isinstance(value, dict):
        v_len = len(value)
        if v_len == 1:
            k, v = list(value.items())[0]
            if k == 'name':
                return SharedVolume(v)
            return UsedVolume(k, v)
        elif 'path' in value:
            return UsedVolume(**value)
        return SharedVolume(**value)
    raise ValueError(
        'Invalid type; expected a list, tuple, dict, or string type, found {0}.'
        .format(type(value).__name__))