def set_nbytes(self, key, nbytes=None):
    obj = super().__getitem__(key)
    if nbytes is not None:
        obj.attrs['nbytes'] = nbytes
    else:
        obj.attrs['nbytes'] = nbytes = ByteCounter.get_nbytes(obj)
    return nbytes