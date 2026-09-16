def delete_row(self, key, value):
    self.rows = filter(lambda x: x.get(key) != value, self.rows)