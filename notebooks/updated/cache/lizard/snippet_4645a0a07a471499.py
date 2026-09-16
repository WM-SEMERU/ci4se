def get_asset_contents_by_record_type(self, asset_content_record_type):
    return AssetContentList(self._provider_session.
        get_asset_contents_by_record_type(asset_content_record_type), self.
        _config_map)