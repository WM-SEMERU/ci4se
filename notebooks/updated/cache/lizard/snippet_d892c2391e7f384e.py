def sorted(self, key=None, reverse=False):
    return self._transform(transformations.sorted_t(key=key, reverse=reverse))