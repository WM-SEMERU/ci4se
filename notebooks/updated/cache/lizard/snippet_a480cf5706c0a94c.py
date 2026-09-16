def set_parallel_value_for_key(self, key, value):
    if self._remotelib:
        self._remotelib.run_keyword('set_parallel_value_for_key', [key,
            value], {})
    else:
        _PabotLib.set_parallel_value_for_key(self, key, value)