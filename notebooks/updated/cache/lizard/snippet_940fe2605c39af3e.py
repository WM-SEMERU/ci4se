def set_bootdev(self, bootdev, persist=False, uefiboot=None):
    reqbootdev = bootdev
    if bootdev not in boot_devices_write and bootdev not in boot_devices_read:
        raise exc.InvalidParameterValue('Unsupported device ' + repr(bootdev))
    bootdev = boot_devices_write.get(bootdev, bootdev)
    if bootdev == 'None':
        payload = {'Boot': {'BootSourceOverrideEnabled': 'Disabled'}}
    else:
        payload = {'Boot': {'BootSourceOverrideEnabled': 'Continuous' if
            persist else 'Once', 'BootSourceOverrideTarget': bootdev}}
        if uefiboot is not None:
            uefiboot = 'UEFI' if uefiboot else 'Legacy'
            payload['BootSourceOverrideMode'] = uefiboot
    self._do_web_request(self.sysurl, payload, method='PATCH')
    return {'bootdev': reqbootdev}