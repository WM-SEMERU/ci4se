def registry_storage(cls):
    if cls.__registry_storage__ is None:
        raise ValueError('__registry_storage__ must be defined')
    if isinstance(cls.__registry_storage__, WTaskRegistryBase) is False:
        raise TypeError(
            "Property '__registry_storage__' is invalid (must derived from WTaskRegistryBase)"
            )
    return cls.__registry_storage__