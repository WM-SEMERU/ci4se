def get_asset_search_session(self):
    if not self.supports_asset_search():
        raise errors.Unimplemented()
    return sessions.AssetSearchSession(runtime=self._runtime)