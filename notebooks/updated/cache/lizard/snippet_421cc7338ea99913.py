def configure(config=None, bind_in_runtime=True):
    global _INJECTOR
    with _INJECTOR_LOCK:
        if _INJECTOR:
            raise InjectorException('Injector is already configured')
        _INJECTOR = Injector(config, bind_in_runtime=bind_in_runtime)
        logger.debug('Created and configured an injector, config=%s', config)
        return _INJECTOR