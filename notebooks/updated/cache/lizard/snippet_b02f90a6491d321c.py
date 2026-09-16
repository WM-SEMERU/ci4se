def AddImportCallbackBySuffix(path, callback):

    def RemoveCallback():
        with _import_callbacks_lock:
            callbacks = _import_callbacks.get(path)
            if callbacks:
                callbacks.remove(callback)
                if not callbacks:
                    del _import_callbacks[path]
    with _import_callbacks_lock:
        _import_callbacks.setdefault(path, set()).add(callback)
    _InstallImportHookBySuffix()
    return RemoveCallback