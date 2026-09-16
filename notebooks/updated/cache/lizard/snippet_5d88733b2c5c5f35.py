def update(self, configuration=values.unset, unique_name=values.unset):
    data = values.of({'Configuration': serialize.object(configuration),
        'UniqueName': unique_name})
    payload = self._version.update('POST', self._uri, data=data)
    return InstalledAddOnInstance(self._version, payload, sid=self.
        _solution['sid'])