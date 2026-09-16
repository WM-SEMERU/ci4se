def get_module(self, setting_name, warn_only_if_overridden=False,
    accept_deprecated='', suppress_warnings=False, warning_stacklevel=3):
    self._warn_if_deprecated_setting_value_requested(setting_name,
        warn_only_if_overridden, suppress_warnings, warning_stacklevel)
    cache_key = self._make_cache_key(setting_name, accept_deprecated)
    if cache_key in self._modules_cache:
        return self._modules_cache[cache_key]
    raw_value = self.get(setting_name, enforce_type=str, accept_deprecated=
        accept_deprecated, check_if_setting_deprecated=False,
        warn_only_if_overridden=warn_only_if_overridden, suppress_warnings=
        suppress_warnings, warning_stacklevel=warning_stacklevel + 1)
    try:
        result = self._do_import(raw_value)
        self._modules_cache[cache_key] = result
        return result
    except ImportError:
        self._raise_setting_value_error(setting_name=setting_name,
            user_value_error_class=OverrideValueNotImportable,
            default_value_error_class=DefaultValueNotImportable,
            additional_text=
            "No module could be found matching the path '{value}'. Please use a full (not relative) import path in the format: 'project.app.module'."
            , value=raw_value)