def _isProtein(self):
    last = self.blockCount - 1
    return self.tEnd == self.tStarts[last] + 3 * self.blockSizes[last
        ] and self.strand == '+' or self.tStart == self.tSize - (self.
        tStarts[last] + 3 * self.blockSizes[last]) and self.strand == '-'