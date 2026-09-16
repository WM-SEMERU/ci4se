def remove_child_catalog(self, catalog_id, child_id):
    if self._catalog_session is not None:
        return self._catalog_session.remove_child_catalog(catalog_id=
            catalog_id, child_id=child_id)
    return self._hierarchy_session.remove_child(id_=catalog_id, child_id=
        child_id)