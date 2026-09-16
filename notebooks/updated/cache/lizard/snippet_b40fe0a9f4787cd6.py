def __flip(self, sliceimg):
    if self.flipH:
        sliceimg = sliceimg[:, -1:0:-1]
    if self.flipV:
        sliceimg = sliceimg[-1:0:-1, :]
    return sliceimg