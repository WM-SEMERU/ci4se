def register(self, *actions):
    assert self.installed(), 'Actions not enabled on this application'
    assert all(isinstance(a, Action) for a in actions)
    for action in actions:
        cat = action.category
        reg = self._state['categories'].setdefault(cat, [])
        reg.append(action)