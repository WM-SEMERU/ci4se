def get_dict_of_dicts(self, key, is_optional=False, is_secret=False,
    is_local=False, default=None, options=None):
    value = self.get_dict(key=key, is_optional=is_optional, is_secret=
        is_secret, is_local=is_local, default=default, options=options)
    if not value:
        return default
    for k in value:
        if not isinstance(value[k], Mapping):
            raise RheaError(
                '`{}` must be an object. Received a non valid configuration for key `{}`.'
                .format(value[k], key))
    return value