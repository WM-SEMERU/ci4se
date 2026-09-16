def reset_bios_to_default(self):
    sushy_system = self._get_sushy_system(PROLIANT_SYSTEM_ID)
    try:
        sushy_system.bios_settings.update_bios_to_default()
    except sushy.exceptions.SushyError as e:
        msg = self._(
            'The Redfish controller is unable to update bios settings to default Error %(error)s'
            ) % {'error': str(e)}
        LOG.debug(msg)
        raise exception.IloError(msg)