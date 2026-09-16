def read_prov(self, document_id=None):
    if document_id:
        if not self.abstract:
            raise ImmutableDocumentException()
        self._id = document_id
    if self.abstract:
        raise AbstractDocumentException()
    self._prov = self._api.get_document_prov(self.id)
    return self._prov