def copy(self):
    self_copy = self.dup()
    self_copy._scopes = copy.copy(self._scopes)
    return self_copy