def get_asset_contents_for_asset(self, asset_id):
    return AssetContentList(self._provider_session.
        get_asset_contents_for_asset(asset_id), self._config_map)