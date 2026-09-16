def set_if_unset(self, key, value):
    if key not in self._conf_dict:
        self.set(key, value)
    return self