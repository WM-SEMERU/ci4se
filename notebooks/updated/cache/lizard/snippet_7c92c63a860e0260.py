def insert(self, key, value):
    if len(self.history) == self.maxsize:
        expectorate = self.history[0]
    else:
        expectorate = None
    self.history.append((key, value))
    if key in self:
        super().__getitem__(key).append(value)
    else:
        super().__setitem__(key, [value])
    if expectorate is not None:
        old_key, old_value = expectorate
        super().__getitem__(old_key).pop(0)
        if len(super().__getitem__(old_key)) == 0:
            super().__delitem__(old_key)
        return old_key, old_value