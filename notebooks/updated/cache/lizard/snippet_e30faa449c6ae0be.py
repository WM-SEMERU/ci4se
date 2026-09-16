async def create_user(self, device_type):
    result = await self.request('post', '', {'devicetype': device_type},
        auth=False)
    self.username = result[0]['success']['username']
    return self.username