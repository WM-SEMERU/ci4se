def _should_set(self, key, mode):
    if mode is None or mode not in ['nx', 'xx']:
        return True
    if mode == 'nx':
        if key in self.redis:
            return False
    elif key not in self.redis:
        return False
    return True