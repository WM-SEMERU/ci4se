def setConfiguration(self, configuration):
    r
    if isinstance(configuration, Configuration):
        configuration = configuration.value
    self.dev.set_configuration(configuration)