def get_asset_query_session(self, proxy=None):
    return AssetQuerySession(self._provider_manager.get_asset_query_session
        (proxy), self._config_map)