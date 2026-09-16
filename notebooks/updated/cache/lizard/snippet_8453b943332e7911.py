def _del_db(self, key, branch, turn, tick):
    self._set_db(key, branch, turn, tick, None)