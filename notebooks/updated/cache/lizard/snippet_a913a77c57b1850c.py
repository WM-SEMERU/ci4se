def enabled(name, **kwargs):
    if _service_is_upstart(name):
        return _upstart_is_enabled(name)
    elif _service_is_sysv(name):
        return _sysv_is_enabled(name)
    return None