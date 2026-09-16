async def ListFilesystems(self, filters):
    _params = dict()
    msg = dict(type='Storage', request='ListFilesystems', version=4, params
        =_params)
    _params['filters'] = filters
    reply = await self.rpc(msg)
    return reply