def has_child_vaults(self, vault_id):
    if self._catalog_session is not None:
        return self._catalog_session.has_child_catalogs(catalog_id=vault_id)
    return self._hierarchy_session.has_children(id_=vault_id)