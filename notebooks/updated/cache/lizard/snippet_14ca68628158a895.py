def sci(self):
    if self._sci_api is None:
        self._sci_api = self.get_sci_api()
    return self._sci_api