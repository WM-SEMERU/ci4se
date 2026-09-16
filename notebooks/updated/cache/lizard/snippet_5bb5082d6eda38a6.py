def getint(self, key, **kwargs):
    return self.get(key, cast_func=int, **kwargs)