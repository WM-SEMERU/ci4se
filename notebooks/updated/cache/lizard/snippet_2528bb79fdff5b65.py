async def probe(self):
    resp = await self._execute(self._adapter.probe_sync)
    _raise_error(None, 'probe', resp)