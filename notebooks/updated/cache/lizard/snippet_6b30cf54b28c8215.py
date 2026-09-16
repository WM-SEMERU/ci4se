def compare_and_set(self, expect, update):
    with self._lock.exclusive:
        if self._value == expect:
            self._value = update
            return True
        return False