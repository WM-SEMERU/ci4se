def select(self, *columns):
    if not columns:
        columns = ['*']
    self.columns = list(columns)
    return self