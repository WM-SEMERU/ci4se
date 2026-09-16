def actions(self):
    if self._actions is None:
        self._actions = list(self.iter_actions())
    return self._actions