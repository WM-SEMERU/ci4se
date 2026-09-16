def get_rec_dtype(self, **keys):
    colnums = keys.get('colnums', None)
    vstorage = keys.get('vstorage', self._vstorage)
    if colnums is None:
        colnums = self._extract_colnums()
    descr = []
    isvararray = numpy.zeros(len(colnums), dtype=numpy.bool)
    for i, colnum in enumerate(colnums):
        dt, isvar = self.get_rec_column_descr(colnum, vstorage)
        descr.append(dt)
        isvararray[i] = isvar
    dtype = numpy.dtype(descr)
    offsets = numpy.zeros(len(colnums), dtype='i8')
    for i, n in enumerate(dtype.names):
        offsets[i] = dtype.fields[n][1]
    return dtype, offsets, isvararray