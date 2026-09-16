def set_hyperparameters(self, hyperparameters):
    self._hyperparameters.update(hyperparameters)
    if self._class:
        LOGGER.debug('Creating a new primitive instance for %s', self.name)
        self.instance = self.primitive(**self._hyperparameters)