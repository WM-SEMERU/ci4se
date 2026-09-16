def get_document(self, doc_uri):
    return self._docs.get(doc_uri) or self._create_document(doc_uri)