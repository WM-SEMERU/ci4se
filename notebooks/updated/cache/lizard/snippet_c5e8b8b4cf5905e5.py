def get_float(self, key, is_list=False, is_optional=False, is_secret=False,
    is_local=False, default=None, options=None):
    if is_list:
        return self._get_typed_list_value(key=key, target_type=float,
            type_convert=float, is_optional=is_optional, is_secret=
            is_secret, is_local=is_local, default=default, options=options)
    return self._get_typed_value(key=key, target_type=float, type_convert=
        float, is_optional=is_optional, is_secret=is_secret, is_local=
        is_local, default=default, options=options)