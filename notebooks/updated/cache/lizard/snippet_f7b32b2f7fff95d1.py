def has_parent_logs(self, log_id):
    if self._catalog_session is not None:
        return self._catalog_session.has_parent_catalogs(catalog_id=log_id)
    return self._hierarchy_session.has_parents(id_=log_id)