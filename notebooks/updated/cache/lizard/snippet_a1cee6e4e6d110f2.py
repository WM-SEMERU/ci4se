def bind_to_provider(self, cls, provider):
    self._check_class(cls)
    if provider is None:
        raise InjectorException('Provider cannot be None, key=%s' % cls)
    self._bindings[cls] = provider
    logger.debug('Bound %s to a provider %s', cls, provider)
    return self