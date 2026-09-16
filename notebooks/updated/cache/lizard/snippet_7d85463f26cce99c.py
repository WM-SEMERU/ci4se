def _call_scope(self, scope, *args, **kwargs):
    result = getattr(self._model, scope)(self, *args, **kwargs)
    return result or self