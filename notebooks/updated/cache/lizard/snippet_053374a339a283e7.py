def getcolnp(self, columnname, nparray, startrow=0, nrow=-1, rowincr=1):
    if not nparray.flags.c_contiguous or nparray.size == 0:
        raise ValueError("Argument 'nparray' has to be a contiguous " +
            'numpy array')
    return self._getcolvh(columnname, startrow, nrow, rowincr, nparray)