def trim_empty_rows(self):
    if self.nrows != 0:
        row_index = 0
        for row_index, row in enumerate(reversed(self.rows)):
            if not self.is_row_empty(row):
                break
        self.nrows = len(self.rows) - row_index
        self.rows = self.rows[:self.nrows]
    return self