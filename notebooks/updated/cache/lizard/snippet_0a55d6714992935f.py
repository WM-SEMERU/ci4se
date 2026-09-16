def iter(self):
    reads = iter(self.reads)
    first = True
    for filename in self.filenames:
        if first:
            first = False
            reader = self._reader
        else:
            reader = self._getReader(filename, self.scoreClass)
        for readAlignments in reader.readAlignments(reads):
            yield readAlignments
    for read in reads:
        yield ReadAlignments(read, [])