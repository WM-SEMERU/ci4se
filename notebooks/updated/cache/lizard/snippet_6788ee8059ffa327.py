def refresh(self):
    self._bundles = {}
    bundles = self._api.get_bundles(self._document.id)
    for bundle in bundles:
        self._bundles[bundle['identifier']] = Bundle(self._api, self.
            _document, bundle)
    return self