def indexcol(self, col: str):
    try:
        self.df[col] = self.df.index.values
    except Exception as e:
        self.err(e)
        return
    self.ok('Column', col, 'added from the index')