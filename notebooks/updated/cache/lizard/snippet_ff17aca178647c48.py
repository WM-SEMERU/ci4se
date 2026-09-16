def __get_activator_method(self, method_name):
    activator = getattr(self.__module, ACTIVATOR, None)
    if activator is None:
        activator = getattr(self.__module, ACTIVATOR_LEGACY, None)
        if activator is not None:
            _logger.warning(
                "Bundle %s uses the deprecated '%s' to declare its activator. Use @BundleActivator instead."
                , self.__name, ACTIVATOR_LEGACY)
    return getattr(activator, method_name, None)