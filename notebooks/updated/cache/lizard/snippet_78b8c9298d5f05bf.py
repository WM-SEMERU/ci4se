async def heater_control(self, device_id, fan_status=None, power_status=None):
    heater = self.heaters.get(device_id)
    if heater is None:
        _LOGGER.error('No such device')
        return
    if fan_status is None:
        fan_status = heater.fan_status
    if power_status is None:
        power_status = heater.power_status
    operation = 0 if fan_status == heater.fan_status else 4
    payload = {'subDomain': heater.sub_domain, 'deviceId': device_id,
        'testStatus': 1, 'operation': operation, 'status': power_status,
        'windStatus': fan_status, 'holdTemp': heater.set_temp, 'tempType': 
        0, 'powerLevel': 0}
    await self.request('deviceControl', payload)