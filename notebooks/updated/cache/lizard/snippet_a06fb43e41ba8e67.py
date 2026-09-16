def filter(self, **kwargs):
    keys = self.filter_keys(**kwargs)
    return self.keys_to_values(keys)