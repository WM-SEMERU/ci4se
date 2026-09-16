async def workerType(self, *args, **kwargs):
    return await self._makeApiCall(self.funcinfo['workerType'], *args, **kwargs
        )