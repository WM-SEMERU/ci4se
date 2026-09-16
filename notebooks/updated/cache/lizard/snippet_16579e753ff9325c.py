def with_row(self, row):
    self = self.copy()
    self.append(row)
    return self