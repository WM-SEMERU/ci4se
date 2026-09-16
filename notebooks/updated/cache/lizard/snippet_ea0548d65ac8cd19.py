def select(self, axis, index, force_copy: bool=False):
    if axis == 0:
        if index == slice(None) and not force_copy:
            return self
        return self[index]
    else:
        raise ValueError('In Histogram1D.select(), axis must be 0.')