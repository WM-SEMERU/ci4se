def object(self, key):
    return _object.Object(self._name, key, context=self._context)