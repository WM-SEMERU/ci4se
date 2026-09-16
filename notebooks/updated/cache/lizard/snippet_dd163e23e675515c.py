def configurations(self):
    if self._configuration_manager is None:
        self._configuration_manager = ConfigurationManager(session=self.
            _session)
    return self._configuration_manager