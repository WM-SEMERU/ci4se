def get(self, key, confidence=0):
    if key not in self.info:
        return None
    conf, value = self.info.get(key)
    if conf >= confidence:
        return value
    return None