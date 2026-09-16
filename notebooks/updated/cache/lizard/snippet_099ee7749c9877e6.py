def add_root_bin(self, bin_id):
    if self._catalog_session is not None:
        return self._catalog_session.add_root_catalog(catalog_id=bin_id)
    return self._hierarchy_session.add_root(id_=bin_id)