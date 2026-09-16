def remove_root_book(self, book_id):
    if self._catalog_session is not None:
        return self._catalog_session.remove_root_catalog(catalog_id=book_id)
    return self._hierarchy_session.remove_root(id_=book_id)