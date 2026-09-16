def write(self, handle):
    handle.write('\t'.join(self.columns))
    handle.write('\n')
    for row in self.rows:
        row.write(handle)