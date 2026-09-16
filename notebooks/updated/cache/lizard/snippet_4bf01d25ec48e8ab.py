def fetch(self):
    params = values.of({})
    payload = self._version.fetch('GET', self._uri, params=params)
    return InstalledAddOnExtensionInstance(self._version, payload,
        installed_add_on_sid=self._solution['installed_add_on_sid'], sid=
        self._solution['sid'])