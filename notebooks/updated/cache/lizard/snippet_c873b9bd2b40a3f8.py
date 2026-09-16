def add_child_book(self, book_id, child_id):
    if self._catalog_session is not None:
        return self._catalog_session.add_child_catalog(catalog_id=book_id,
            child_id=child_id)
    return self._hierarchy_session.add_child(id_=book_id, child_id=child_id)