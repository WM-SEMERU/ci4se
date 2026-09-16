def add_bundle(self, prov_bundle, identifier):
    if self.abstract:
        raise AbstractDocumentException()
    self._api.add_bundle(self.id, prov_bundle.serialize(), identifier)