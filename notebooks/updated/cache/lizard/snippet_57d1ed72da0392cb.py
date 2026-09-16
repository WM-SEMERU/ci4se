def intersect(self, enumerable, key=lambda x: x):
    if not isinstance(enumerable, Enumerable3):
        raise TypeError(
            'enumerable parameter must be an instance of Enumerable')
    return self.join(enumerable, key, key).select(lambda x: x[0])