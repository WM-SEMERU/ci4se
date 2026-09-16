def get_asset_notification_session_for_repository(self, asset_receiver=None,
    repository_id=None, proxy=None):
    return (self._provider_manager.
        get_asset_notification_session_for_repository(asset_receiver,
        repository_id, proxy))