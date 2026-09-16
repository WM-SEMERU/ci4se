def get_fresh(self, key, default=None, cast=None):
    return self.get(key, default=default, cast=cast, fresh=True)