def insert(self, action: Action, where: 'Union[int, Delegate.Where]'):
    if isinstance(where, int):
        self.actions.insert(where, action)
        return
    here = where(self.actions)
    self.actions.insert(here, action)