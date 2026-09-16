def _validate_importers(importers):
    if importers is None:
        return None

    def _to_importer(priority, func):
        assert isinstance(priority, int), priority
        assert callable(func), func
        return priority, _importer_callback_wrapper(func)
    return tuple(_to_importer(priority, func) for priority, func in importers)