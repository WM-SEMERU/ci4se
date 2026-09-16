def detach(self):
    info = self._registry.get(self)
    obj = info and info.weakref()
    if obj is not None and self._registry.pop(self, None):
        return obj, info.func, info.args, info.kwargs or {}