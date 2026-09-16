def _configure_injector(self, modules):
    self._register()
    self._create_injector()
    self._bind_core()
    self._bind_modules(modules)
    self.logger.debug('Injector configuration with modules {0}.'.format(
        modules))
    self._dependencies_initialized = True