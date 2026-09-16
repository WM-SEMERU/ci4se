def dec(self, key, delta=1):
    self.set(key, (self.get(key) or 0) - delta)