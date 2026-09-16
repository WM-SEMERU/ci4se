def _read_args_from_h5ad(adata: AnnData=None, filename: Optional[PathLike]=
    None, mode: Optional[str]=None, chunk_size: int=6000):
    if filename is None and (adata is None or adata.filename is None):
        raise ValueError(
            'Need either a filename or an AnnData object with file backing')
    backed = mode is not None
    if filename is None and not backed:
        filename = adata.filename
    d = {}
    if backed:
        f = adata.file._file
    else:
        f = h5py.File(filename, 'r')
    for key in f.keys():
        if backed and key in AnnData._BACKED_ATTRS:
            d[key] = None
        else:
            _read_key_value_from_h5(f, d, key, chunk_size=chunk_size)
    if 'X' not in d:
        if backed == 'r+':
            for key in AnnData._H5_ALIASES['X']:
                if key in d:
                    del f[key]
                    f.create_dataset('X', data=d[key])
                    break
    csr_keys = [key.replace('_csr_data', '') for key in d if '_csr_data' in key
        ]
    for key in csr_keys:
        d = load_sparse_csr(d, key=key)
    if not backed:
        f.close()
    return AnnData._args_from_dict(d)