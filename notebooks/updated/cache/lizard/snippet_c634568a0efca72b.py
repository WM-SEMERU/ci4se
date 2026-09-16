async def getWorkerType(self, *args, **kwargs):
    return await self._makeApiCall(self.funcinfo['getWorkerType'], *args,
        **kwargs)