def gt(self, key, value, includeMissing=False):
    self.table, self.index_track = internal.select(self.table, self.
        index_track, key, self.GREATER, value, includeMissing)
    return self