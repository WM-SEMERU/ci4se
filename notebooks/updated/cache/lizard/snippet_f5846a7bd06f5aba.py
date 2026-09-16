async def get_constants(self):
    url = self.BASE + '/constants'
    data = await self.request(url)
    return Constants(self, data)