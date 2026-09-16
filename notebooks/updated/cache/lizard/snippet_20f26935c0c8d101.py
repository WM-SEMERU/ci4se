def find_next(self, *strings, **kwargs):
    start = kwargs.pop('start', None)
    keys_only = kwargs.pop('keys_only', False)
    staht = start if start is not None else self.cursor
    for start, stop in [(staht, len(self)), (0, staht)]:
        for i in range(start, stop):
            for string in strings:
                if string in self[i]:
                    tup = i, self[i]
                    self.cursor = i + 1
                    if keys_only:
                        return i
                    return tup