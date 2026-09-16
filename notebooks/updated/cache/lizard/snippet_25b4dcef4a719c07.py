def set_bios_settings(self, data=None, only_allowed_settings=True):
    if not data:
        raise exception.IloError('Could not apply settings with empty data')
    if only_allowed_settings:
        unsupported_settings = [key for key in data if key not in constants
            .SUPPORTED_BIOS_PROPERTIES]
        if unsupported_settings:
            msg = (
                'Could not apply settings as one or more settings are not supported. Unsupported settings are %s. Supported settings are %s.'
                 % (unsupported_settings, constants.SUPPORTED_BIOS_PROPERTIES))
            raise exception.IloError(msg)
    self._change_bios_setting(data)