def _init_backends(self):
    self._backends = {}
    for section in self._config.sections():
        section_components = section.rsplit('.', 1)
        if section_components[0] == 'auth.backends':
            auth_backend = section_components[1]
            self._backends[auth_backend] = eval(self._config.get(section,
                'type'))
    self._logger.debug('Registered auth backends %s' % str(self._backends))