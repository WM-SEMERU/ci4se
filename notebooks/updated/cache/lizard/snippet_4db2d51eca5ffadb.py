def _dict_native_ok(d):
    if len(d) >= 256:
        return False
    for k in d:
        if not isinstance(k, six.string_types):
            return False
    return True