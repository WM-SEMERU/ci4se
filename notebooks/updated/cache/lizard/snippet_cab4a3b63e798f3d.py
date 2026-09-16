def add(self, string: (str, list)):
    if len(self._entries) == 1:
        self._entries[0].delete(0, 'end')
        self._entries[0].insert(0, string)
    else:
        if len(string) != len(self._entries):
            raise ValueError(
                'the "string" list must be equal to the number of entries')
        for i, e in enumerate(self._entries):
            self._entries[i].delete(0, 'end')
            self._entries[i].insert(0, string[i])