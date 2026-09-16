def is_parent_of_vault(self, id_, vault_id):
    if self._catalog_session is not None:
        return self._catalog_session.is_parent_of_catalog(id_=id_,
            catalog_id=vault_id)
    return self._hierarchy_session.is_parent(id_=vault_id, parent_id=id_)