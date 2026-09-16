def has_parent_catalogs(self, catalog_id):
    if self._catalog_session is not None:
        return self._catalog_session.has_parent_catalogs(catalog_id=catalog_id)
    return self._hierarchy_session.has_parents(id_=catalog_id)