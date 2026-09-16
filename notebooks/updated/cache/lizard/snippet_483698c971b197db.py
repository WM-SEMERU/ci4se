def get_input(self, value, _search=None):
    if _search is None:
        if isinstance(value, string_types):
            _search = lambda s: s.name
        elif isinstance(value, type):
            _search = type
    for i in self.inputs:
        step = i.get_input(value, _search)
        if step is not None:
            return step
    if _search(self) == value:
        return self