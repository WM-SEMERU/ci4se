def get_setting(key, **kwargs):
    has_default = 'default' in kwargs
    default_val = kwargs.get('default')
    try:
        if has_default:
            return getattr(settings, key, default_val)
        else:
            return getattr(settings, key)
    except Exception as e:
        raise ImproperlyConfigured(_(
            '"{0}" setting has not been properly set. {1}').format(key, e))