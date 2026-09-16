def _index(self, row):
    self.rows.append(row)
    self._keys.update(row.keys())
    self._steps += 1