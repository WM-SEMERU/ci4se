async def sqsStats(self, *args, **kwargs):
    return await self._makeApiCall(self.funcinfo['sqsStats'], *args, **kwargs)