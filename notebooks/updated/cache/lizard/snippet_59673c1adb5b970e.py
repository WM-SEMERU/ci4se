def intersect(self, range2):
    if not self.overlaps(range2):
        return None
    return type(self)(self.chr, max(self.start, range2.start) + self.
        _start_offset, min(self.end, range2.end), self.payload, self.dir)