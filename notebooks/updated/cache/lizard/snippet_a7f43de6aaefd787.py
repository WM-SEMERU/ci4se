def get_authorizations_by_vault(self, vault_id):
    mgr = self._get_provider_manager('AUTHORIZATION', local=True)
    lookup_session = mgr.get_authorization_lookup_session_for_vault(vault_ids,
        proxy=self._proxy)
    lookup_session.use_isolated_vault_view()
    return lookup_session.get_authorizations()