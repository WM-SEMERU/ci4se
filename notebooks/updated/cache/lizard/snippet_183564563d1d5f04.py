def column(self, key):
    for row in self.rows:
        if key in row:
            yield row[key]