def get_asset_content_form_for_create(self, asset_id=None,
    asset_content_record_types=None):
    if AWS_ASSET_CONTENT_RECORD_TYPE in asset_content_record_types:
        asset_content_record_types.remove(AWS_ASSET_CONTENT_RECORD_TYPE)
        return AssetContentForm(self._provider_session.
            get_asset_content_form_for_create(asset_id,
            asset_content_record_types), self._config_map, self.
            get_repository_id())
    else:
        return self._provider_session.get_asset_content_form_for_create(
            asset_id, asset_content_record_types)