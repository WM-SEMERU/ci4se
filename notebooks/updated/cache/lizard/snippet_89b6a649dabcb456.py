def get(pb_or_dict, key, default=_SENTINEL):
    key, subkey = _resolve_subkeys(key)
    if isinstance(pb_or_dict, Message):
        answer = getattr(pb_or_dict, key, default)
    elif isinstance(pb_or_dict, collections.Mapping):
        answer = pb_or_dict.get(key, default)
    else:
        raise TypeError(
            'Tried to fetch a key %s on an invalid object; expected a dict or protobuf message.'
            )
    if answer is _SENTINEL:
        raise KeyError(key)
    if subkey and answer is not default:
        return get(answer, subkey, default=default)
    return answer