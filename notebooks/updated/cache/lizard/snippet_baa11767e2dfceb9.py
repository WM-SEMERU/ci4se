def get_asset_contents_by_genus_type_for_asset(self,
    asset_content_genus_type, asset_id):
    return AssetContentList(self._provider_session.
        get_asset_contents_by_genus_type_for_asset(asset_content_genus_type,
        asset_id), self._config_map)