def add_root_catalog(self, catalog_id):
    if self._catalog_session is not None:
        return self._catalog_session.add_root_catalog(catalog_id=catalog_id)
    return self._hierarchy_session.add_root(id_=catalog_id)