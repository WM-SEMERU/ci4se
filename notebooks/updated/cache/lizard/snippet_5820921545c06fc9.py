def next(self):
    row = self.reader.next()
    return [s.decode('utf-8') for s in row]