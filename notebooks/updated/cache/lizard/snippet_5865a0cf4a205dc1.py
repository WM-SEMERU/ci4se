def popall(self, key):
    values = self.getall(key)
    try:
        del self[key]
    except KeyError:
        pass
    return values