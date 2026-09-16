def is_child_of_book(self, id_, book_id):
    if self._catalog_session is not None:
        return self._catalog_session.is_child_of_catalog(id_=id_,
            catalog_id=book_id)
    return self._hierarchy_session.is_child(id_=book_id, child_id=id_)