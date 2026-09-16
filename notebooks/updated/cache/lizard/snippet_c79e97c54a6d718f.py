def get_setting_with_envfallback(setting, default=None, typecast=None):
    try:
        from django.conf import settings
    except ImportError:
        return default
    else:
        fallback = getattr(settings, setting, default)
        value = os.environ.get(setting, fallback)
        if typecast:
            value = typecast(value)
        return value