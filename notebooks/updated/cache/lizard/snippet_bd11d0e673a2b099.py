def remove_child_books(self, book_id):
    if self._catalog_session is not None:
        return self._catalog_session.remove_child_catalogs(catalog_id=book_id)
    return self._hierarchy_session.remove_children(id_=book_id)