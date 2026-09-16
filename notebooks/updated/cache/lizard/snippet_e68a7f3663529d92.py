def get_asset_spatial_assignment_session(self, proxy):
    if not self.supports_asset_spatial_assignment():
        raise Unimplemented()
    try:
        from . import sessions
    except ImportError:
        raise
    proxy = self._convert_proxy(proxy)
    try:
        session = sessions.AssetSpatialAssignmentSession(proxy, runtime=
            self._runtime)
    except AttributeError:
        raise
    return session