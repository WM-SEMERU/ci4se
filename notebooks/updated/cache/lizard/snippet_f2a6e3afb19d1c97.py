async def listHookGroups(self, *args, **kwargs):
    return await self._makeApiCall(self.funcinfo['listHookGroups'], *args,
        **kwargs)