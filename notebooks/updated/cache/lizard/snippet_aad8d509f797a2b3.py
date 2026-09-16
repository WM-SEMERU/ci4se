def version(self):
    return self.get_json(URL_VERSION.format(self._url), astext=True)