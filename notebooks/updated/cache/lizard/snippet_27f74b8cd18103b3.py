def get_config(name='root'):
    try:
        config = snapper.GetConfig(name)
        return config
    except dbus.DBusException as exc:
        raise CommandExecutionError(
            'Error encountered while retrieving configuration: {0}'.format(
            _dbus_exception_to_reason(exc, locals())))