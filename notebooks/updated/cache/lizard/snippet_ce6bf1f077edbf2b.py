def get_asset_composition_session(self):
    if not self.supports_asset_composition():
        raise Unimplemented()
    try:
        from . import sessions
    except ImportError:
        raise
    try:
        session = sessions.AssetCompositionSession(proxy=self._proxy,
            runtime=self._runtime)
    except AttributeError:
        raise
    return session