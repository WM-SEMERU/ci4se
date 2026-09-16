def initialize(self, init_value, context=None, force=False):
    if not force and self._instance is not None:
        raise ConfigurationAlreadyInitializedError(
            'Configuration manager object is already initialized.')
    self.__class__._instance = Root(init_value, context=context)