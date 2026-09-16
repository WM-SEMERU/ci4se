def scopes(self, scopes):
    validate_scopes(scopes)
    self._scopes = ' '.join(set(scopes)) if scopes else ''