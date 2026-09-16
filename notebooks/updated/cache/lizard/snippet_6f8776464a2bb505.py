def _getsetting(setting, default):
    setting = _DJANGO_SETTING_PREFIX + setting
    try:
        return getattr(settings, setting)
    except:
        return default