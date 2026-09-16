def get_and_set(self, value):
    with self._reference.get_lock():
        oldval = self._reference.value
        self._reference.value = value
        return oldval