def state(self, state):
    with self._lock:
        self._value = self._states.index(state)