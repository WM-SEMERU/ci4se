async def FindActionTagsByPrefix(self, prefixes):
    _params = dict()
    msg = dict(type='Action', request='FindActionTagsByPrefix', version=3,
        params=_params)
    _params['prefixes'] = prefixes
    reply = await self.rpc(msg)
    return reply