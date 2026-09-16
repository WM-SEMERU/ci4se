def get_bins_by_resource(self, resource_id):
    mgr = self._get_provider_manager('RESOURCE', local=True)
    lookup_session = mgr.get_bin_lookup_session(proxy=self._proxy)
    return lookup_session.get_bins_by_ids(self.get_bin_ids_by_resource(
        resource_id))