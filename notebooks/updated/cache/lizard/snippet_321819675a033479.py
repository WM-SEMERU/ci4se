def announce_urls(self, default=[]):
    try:
        response = self._engine._rpc.t.multicall(self._fields['hash'], 0,
            't.url=', 't.is_enabled=')
    except xmlrpc.ERRORS as exc:
        raise error.EngineError('While getting announce URLs for #%s: %s' %
            (self._fields['hash'], exc))
    if response:
        return [i[0] for i in response if i[1]]
    else:
        return default