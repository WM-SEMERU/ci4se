async def _write(self, path, data, *, flags=None, cas=None, acquire=None,
    release=None):
    if not isinstance(data, bytes):
        raise ValueError('value must be bytes')
    path = '/v1/kv/%s' % path
    response = await self._api.put(path, params={'flags': flags, 'cas': cas,
        'acquire': acquire, 'release': release}, data=data, headers={
        'Content-Type': 'application/octet-stream'})
    return response