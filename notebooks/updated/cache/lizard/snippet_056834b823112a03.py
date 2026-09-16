def get_child_repository_ids(self, repository_id):
    if self._catalog_session is not None:
        return self._catalog_session.get_child_catalog_ids(catalog_id=
            repository_id)
    return self._hierarchy_session.get_children(id_=repository_id)