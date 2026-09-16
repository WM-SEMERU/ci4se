def remove_child_banks(self, bank_id):
    if self._catalog_session is not None:
        return self._catalog_session.remove_child_catalogs(catalog_id=bank_id)
    return self._hierarchy_session.remove_children(id_=bank_id)