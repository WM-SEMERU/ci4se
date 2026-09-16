async def findArtifactFromTask(self, *args, **kwargs):
    return await self._makeApiCall(self.funcinfo['findArtifactFromTask'], *
        args, **kwargs)