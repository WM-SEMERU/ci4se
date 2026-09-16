def move_to_top(self):
    self.current_item = self.root
    for f in self._hooks['top']:
        f(self)
    return self