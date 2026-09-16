def _proxy(self):
    if self._context is None:
        self._context = ExportConfigurationContext(self._version,
            resource_type=self._solution['resource_type'])
    return self._context