def remove(self):
    if self._own_index is not None and self.parent:
        self.parent.pop(self._own_index)
    return self