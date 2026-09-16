def get_asset_contents_by_ids(self, asset_content_ids):
    return AssetContentList(self._provider_session.
        get_asset_contents_by_ids(asset_content_ids), self._config_map)