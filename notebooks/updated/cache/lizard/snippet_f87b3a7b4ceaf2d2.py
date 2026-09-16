def init(self, key_value_pairs=None, **kwargs):
    if key_value_pairs is None:
        key_value_pairs = kwargs
    return [self.set(k, v) for k, v in key_value_pairs.items() if k not in self
        ]