def append_var(var, value):
    makeconf = _get_makeconf()
    old_value = get_var(var)
    if old_value is not None:
        appended_value = '{0} {1}'.format(old_value, value)
        __salt__['file.sed'](makeconf, '^{0}=.*'.format(var), '{0}="{1}"'.
            format(var, appended_value))
    else:
        _add_var(var, value)
    new_value = get_var(var)
    return {var: {'old': old_value, 'new': new_value}}