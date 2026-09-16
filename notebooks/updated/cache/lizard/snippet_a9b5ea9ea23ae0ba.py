def get_parent_log_ids(self, log_id):
    if self._catalog_session is not None:
        return self._catalog_session.get_parent_catalog_ids(catalog_id=log_id)
    return self._hierarchy_session.get_parents(id_=log_id)