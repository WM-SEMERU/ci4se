def positionlesscrop(self, x, y, sheet_coord_system):
    slice_inds = self.findinputslice(sheet_coord_system.sheet2matrixidx(x,
        y), self.shape_on_sheet(), sheet_coord_system.shape)
    self.set(slice_inds)