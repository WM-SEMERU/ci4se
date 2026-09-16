def data(self):
    return self.mmap[self.content_offset + self._offset:self._offset + self
        .size]