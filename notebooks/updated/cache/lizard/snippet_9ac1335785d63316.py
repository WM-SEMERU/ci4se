def changed(self, *value):
    if self._last_checked_value != value:
        self._last_checked_value = value
        return True
    return False