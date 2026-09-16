def _ensure_counter(self):
    if self._counter_path not in self._client.kv:
        self._client.kv[self._counter_path] = ''.zfill(self._COUNTER_FILL)