def get_supported_boot_mode(self):
    sushy_system = self._get_sushy_system(PROLIANT_SYSTEM_ID)
    try:
        return SUPPORTED_BOOT_MODE_MAP.get(sushy_system.supported_boot_mode)
    except sushy.exceptions.SushyError as e:
        msg = self._(
            'The Redfish controller failed to get the supported boot modes. Error: %s'
            ) % e
        LOG.debug(msg)
        raise exception.IloError(msg)