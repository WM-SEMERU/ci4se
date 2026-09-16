def data(self, column, role):
    return self.columns[column](self._user, role)