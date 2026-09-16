def vphi(self, *args, **kwargs):
    thiso = self(*args, **kwargs)
    if not len(thiso.shape) == 2:
        thiso = thiso.reshape((thiso.shape[0], 1))
    return thiso[(2), :] / thiso[(0), :]