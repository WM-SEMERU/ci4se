def sort_index(self, ascending=True):
    if isinstance(self.index, MultiIndex):
        raise NotImplementedError(
            'Weld does not yet support sorting on multiple columns')
    return self.sort_values(self.index._gather_names(), ascending)