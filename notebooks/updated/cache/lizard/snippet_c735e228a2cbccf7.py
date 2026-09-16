def add(self, name, func):
    if name not in self.hooks:
        raise ValueError('Unknown hook name %s' % name)
    was_empty = self._empty()
    self.hooks[name].append(func)
    if self.app and was_empty and not self._empty():
        self.app.reset()