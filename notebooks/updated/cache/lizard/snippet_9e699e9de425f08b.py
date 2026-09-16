def __query(p, k, v, accepted_keys=None, required_values=None, path=None,
    exact=True):

    def as_values_iterable(v):
        if isinstance(v, dict):
            return v.values()
        elif isinstance(v, six.string_types):
            return [v]
        else:
            return v
    if path and path != p:
        return False
    if accepted_keys:
        if isinstance(accepted_keys, six.string_types):
            accepted_keys = [accepted_keys]
        if len([akey for akey in accepted_keys if akey == k or not exact and
            akey in k]) == 0:
            return False
    if required_values:
        if isinstance(required_values, six.string_types):
            required_values = [required_values]
        if len(required_values) > len([term for term in required_values for
            nv in as_values_iterable(v) if term == nv or not exact and term in
            nv]):
            return False
    return True