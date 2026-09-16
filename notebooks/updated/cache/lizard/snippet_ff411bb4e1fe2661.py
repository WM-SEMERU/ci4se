def add_object(self, obj, properties=()):
    self._objects.add(obj)
    self._properties |= properties
    self._pairs.update((obj, p) for p in properties)