async def workerTypeErrors(self, *args, **kwargs):
    return await self._makeApiCall(self.funcinfo['workerTypeErrors'], *args,
        **kwargs)