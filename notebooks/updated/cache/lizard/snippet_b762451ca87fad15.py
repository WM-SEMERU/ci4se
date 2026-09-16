def iter_adapters():
    adapters = adapter_catalog.values()
    return sorted(adapters, key=lambda a: a.model.__name__)