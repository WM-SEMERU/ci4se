def remove_root_bank(self, bank_id):
    if self._catalog_session is not None:
        return self._catalog_session.remove_root_catalog(catalog_id=bank_id)
    return self._hierarchy_session.remove_root(id_=bank_id)