async def set_heating_level(self, level, duration=0):
    url = '{}/devices/{}'.format(API_URL, self.device.deviceid)
    level = 10 if level < 10 else level
    level = 100 if level > 100 else level
    if self.side == 'left':
        data = {'leftHeatingDuration': duration, 'leftTargetHeatingLevel':
            level}
    elif self.side == 'right':
        data = {'rightHeatingDuration': duration, 'rightTargetHeatingLevel':
            level}
    set_heat = await self.device.api_put(url, data)
    if set_heat is None:
        _LOGGER.error('Unable to set eight heating level.')
    else:
        self.device.handle_device_json(set_heat['device'])