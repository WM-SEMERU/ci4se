def map_values2(self, func):
    return TDict({k: func(k, v) for k, v in self.items()})