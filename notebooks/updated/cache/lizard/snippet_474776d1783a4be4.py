def get_resources_by_bin(self, bin_id):
    mgr = self._get_provider_manager('RESOURCE', local=True)
    lookup_session = mgr.get_resource_lookup_session_for_bin(bin_id, proxy=
        self._proxy)
    lookup_session.use_isolated_bin_view()
    return lookup_session.get_resources()