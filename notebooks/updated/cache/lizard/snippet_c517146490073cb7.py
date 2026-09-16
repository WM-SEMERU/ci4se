def get_asset_temporal_session(self):
    if not self.supports_asset_temporal():
        raise Unimplemented()
    try:
        from . import sessions
    except ImportError:
        raise
    try:
        session = sessions.AssetTemporalSession(proxy=self._proxy, runtime=
            self._runtime)
    except AttributeError:
        raise
    return session