def get_config_object():
    global _DEFAULT_CONFIG_WRAPPER
    if _DEFAULT_CONFIG_WRAPPER is not None:
        return _DEFAULT_CONFIG_WRAPPER
    with _DEFAULT_CONFIG_WRAPPER_LOCK:
        if _DEFAULT_CONFIG_WRAPPER is not None:
            return _DEFAULT_CONFIG_WRAPPER
        _DEFAULT_CONFIG_WRAPPER = ConfigWrapper()
        return _DEFAULT_CONFIG_WRAPPER