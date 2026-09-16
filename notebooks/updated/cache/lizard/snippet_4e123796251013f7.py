def setting(key, default=None, expected_type=None, qsettings=None):
    if default is None:
        default = inasafe_default_settings.get(key, None)
    full_key = '%s/%s' % (APPLICATION_NAME, key)
    return general_setting(full_key, default, expected_type, qsettings)