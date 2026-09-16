def limit(self, max_):
    if isinstance(self, type):
        result = self()
    else:
        result = copy.deepcopy(self)
    result.max_ = max_
    return result