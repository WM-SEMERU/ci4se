async def listTaskGroup(self, *args, **kwargs):
    return await self._makeApiCall(self.funcinfo['listTaskGroup'], *args,
        **kwargs)