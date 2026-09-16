def get_type(self, name, api=None):
    k = name, api
    if k in self.types:
        return self.types[k]
    else:
        return self.types[name, None]