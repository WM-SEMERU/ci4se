def delete(self):
    if self.abstract:
        raise AbstractDocumentException()
    self._api.delete_document(self.id)
    self._id = None
    return True