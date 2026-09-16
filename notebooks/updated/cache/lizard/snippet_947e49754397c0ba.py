def general_setting(key, default=None, expected_type=None, qsettings=None):
    if qsettings is None:
        qsettings = QSettings()
    try:
        if isinstance(expected_type, type):
            return qsettings.value(key, default, type=expected_type)
        else:
            return qsettings.value(key, default)
    except TypeError as e:
        LOGGER.debug('exception %s' % e)
        LOGGER.debug('%s %s %s' % (key, default, expected_type))
        return qsettings.value(key, default)