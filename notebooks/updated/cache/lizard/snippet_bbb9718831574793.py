def dict_of_lists(self):
    result = {}
    for key, value in self._items:
        if key in result:
            result[key].append(value)
        else:
            result[key] = [value]
    return result