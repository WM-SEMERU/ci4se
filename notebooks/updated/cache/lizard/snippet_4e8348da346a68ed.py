def setdefault(self, name, value):
    if name in self:
        return self[name]
    self[name] = value
    return self[name]