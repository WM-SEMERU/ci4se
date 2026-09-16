async def getUpdates(self, offset=None, limit=None, timeout=None,
    allowed_updates=None):
    p = _strip(locals())
    return await self._api_request('getUpdates', _rectify(p))