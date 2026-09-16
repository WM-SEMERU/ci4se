def get_setting(context, key, default_val='', as_key=None):
    if ('%s' % default_val).startswith('$.'):
        default_val = getattr(settings, default_val[2:])
    val = getattr(settings, key, default_val)
    if not as_key:
        return val
    context[as_key] = val
    return ''