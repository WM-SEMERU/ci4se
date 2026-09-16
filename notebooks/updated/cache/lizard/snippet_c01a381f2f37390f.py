def exclude(self, col: str, val):
    try:
        self.df = self.df[self.df[col] != val]
    except Exception as e:
        self.err(e, 'Can not exclude rows based on value ' + str(val))