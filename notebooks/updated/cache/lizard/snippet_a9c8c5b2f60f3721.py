def get_asset_content_lookup_session_for_repository(self, repository_id=None):
    return AssetContentLookupSession(self._provider_manager.
        get_asset_content_lookup_session_for_repository(repository_id),
        self._config_map)