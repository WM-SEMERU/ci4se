def execute_loaders(self, env=None, silent=None, key=None, filename=None):
    if key is None:
        default_loader(self, self._defaults)
    env = (env or self.current_env).upper()
    silent = silent or self.SILENT_ERRORS_FOR_DYNACONF
    settings_loader(self, env=env, silent=silent, key=key, filename=filename)
    self.load_extra_yaml(env, silent, key)
    enable_external_loaders(self)
    for loader in self.loaders:
        self.logger.debug('Dynaconf executing: %s', loader.__name__)
        loader.load(self, env, silent=silent, key=key)
    self.load_includes(env, silent=silent, key=key)
    self.logger.debug('Loaded Files: %s', deduplicate(self._loaded_files))