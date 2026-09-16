def get_asset_query_session(self, proxy):
    if not self.supports_asset_query():
        raise Unimplemented()
    try:
        from . import sessions
    except ImportError:
        raise
    proxy = self._convert_proxy(proxy)
    try:
        session = sessions.AssetQuerySession(proxy=proxy, runtime=self._runtime
            )
    except AttributeError:
        raise
    return session