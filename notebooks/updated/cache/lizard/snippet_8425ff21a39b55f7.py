def get_callback_function(setting_name, default=None):
    func = getattr(settings, setting_name, None)
    if not func:
        return default
    if callable(func):
        return func
    if isinstance(func, str):
        func = import_string(func)
    if not callable(func):
        raise ImproperlyConfigured('{name} must be callable.'.format(name=
            setting_name))
    return func