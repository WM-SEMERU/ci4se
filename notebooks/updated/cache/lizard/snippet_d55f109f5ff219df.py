def _decrypt_object(obj, **kwargs):
    if salt.utils.stringio.is_readable(obj):
        return _decrypt_object(obj.getvalue(), **kwargs)
    if isinstance(obj, six.string_types):
        if re.search(NACL_REGEX, obj) is not None:
            return __salt__['nacl.dec'](re.search(NACL_REGEX, obj).group(1),
                **kwargs)
        else:
            return obj
    elif isinstance(obj, dict):
        for key, value in six.iteritems(obj):
            obj[key] = _decrypt_object(value, **kwargs)
        return obj
    elif isinstance(obj, list):
        for key, value in enumerate(obj):
            obj[key] = _decrypt_object(value, **kwargs)
        return obj
    else:
        return obj