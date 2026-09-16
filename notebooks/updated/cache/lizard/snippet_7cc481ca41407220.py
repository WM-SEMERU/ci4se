async def peers(self):
    response = await self._api.get('/v1/status/peers')
    if response.status == 200:
        return set(response.body)