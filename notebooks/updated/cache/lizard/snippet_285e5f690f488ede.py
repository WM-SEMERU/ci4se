def aspage(self):
    if self.offset is None:
        raise ValueError('cannot return virtual frame as page.')
    self.parent.filehandle.seek(self.offset)
    return TiffPage(self.parent, index=self.index)