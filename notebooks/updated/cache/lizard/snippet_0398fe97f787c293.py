def add_check(self, check):
    if self._add_check_callback is not None:
        if not self._add_check_callback(self, check):
            return False
    self._checkid2index[check.id] = len(self._checks)
    self._checks.append(check)
    return True