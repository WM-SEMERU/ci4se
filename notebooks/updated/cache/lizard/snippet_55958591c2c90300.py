def lt(self, key, value, includeMissing=False):
    self.table, self.index_track = internal.select(self.table, self.
        index_track, key, self.LESS, value, includeMissing)
    return self