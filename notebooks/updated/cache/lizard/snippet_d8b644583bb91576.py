def csv(self):
    lines = self._parsecsv(self.raw)
    keys = next(lines)
    for line in lines:
        yield dict(zip(keys, line))