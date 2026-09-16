async def put(self, tube, data, ttl=None, ttr=None, delay=None):
    cmd = tube.cmd('put')
    args = data,
    params = dict()
    if ttr is not None:
        params['ttr'] = ttr
    if ttl is not None:
        params['ttl'] = ttl
    if delay is not None:
        params['delay'] = delay
    if params:
        args += params,
    res = await self.tnt.call(cmd, args)
    return res