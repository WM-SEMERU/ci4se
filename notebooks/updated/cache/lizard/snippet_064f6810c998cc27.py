def release_value_set(self):
    if self._remotelib:
        self._remotelib.run_keyword('release_value_set', [self._my_id], {})
    else:
        _PabotLib.release_value_set(self, self._my_id)