def dataSetElementType(h5Dataset):
    dtype = h5Dataset.dtype
    if dtype.names:
        return '<structured>'
    elif dtype.metadata and 'vlen' in dtype.metadata:
        vlen_type = dtype.metadata['vlen']
        try:
            return '<vlen {}>'.format(vlen_type.__name__)
        except AttributeError:
            return '<vlen {}>'.format(vlen_type.name)
    return str(dtype)