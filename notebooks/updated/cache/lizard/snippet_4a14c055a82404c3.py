def assign_asset_to_repository(self, asset_id, repository_id):
    mgr = self._get_provider_manager('REPOSITORY', local=True)
    lookup_session = mgr.get_repository_lookup_session(proxy=self._proxy)
    lookup_session.get_repository(repository_id)
    self._assign_object_to_catalog(asset_id, repository_id)