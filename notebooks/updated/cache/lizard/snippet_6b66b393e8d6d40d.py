def devices(self):
    response = self._call(mc_calls.DeviceManagementInfo)
    registered_devices = response.body.get('data', {}).get('items', [])
    return registered_devices