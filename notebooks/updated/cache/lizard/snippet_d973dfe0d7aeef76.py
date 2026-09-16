def check(self, check, value, missing=False):
    fun_name, fun_args, fun_kwargs, default = self._parse_with_caching(check)
    if missing:
        if default is None:
            raise VdtMissingValue()
        value = self._handle_none(default)
    if value is None:
        return None
    return self._check_value(value, fun_name, fun_args, fun_kwargs)