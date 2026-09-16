async def AddCharm(self, channel, url):
    _params = dict()
    msg = dict(type='Client', request='AddCharm', version=1, params=_params)
    _params['channel'] = channel
    _params['url'] = url
    reply = await self.rpc(msg)
    return reply