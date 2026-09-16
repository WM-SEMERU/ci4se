async def set_misc_settings(self, target: str, value: str):
    params = {'settings': [{'target': target, 'value': value}]}
    return await self.services['system']['setDeviceMiscSettings'](params)