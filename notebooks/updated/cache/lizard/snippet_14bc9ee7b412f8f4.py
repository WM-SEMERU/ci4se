async def removeKeyPair(self, *args, **kwargs):
    return await self._makeApiCall(self.funcinfo['removeKeyPair'], *args,
        **kwargs)