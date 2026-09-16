def create(shape, chunks=True, dtype=None, compressor='default', fill_value
    =0, order='C', store=None, synchronizer=None, overwrite=False, path=
    None, chunk_store=None, filters=None, cache_metadata=True, cache_attrs=
    True, read_only=False, object_codec=None, **kwargs):
    store = normalize_store_arg(store)
    compressor, fill_value = _kwargs_compat(compressor, fill_value, kwargs)
    init_array(store, shape=shape, chunks=chunks, dtype=dtype, compressor=
        compressor, fill_value=fill_value, order=order, overwrite=overwrite,
        path=path, chunk_store=chunk_store, filters=filters, object_codec=
        object_codec)
    z = Array(store, path=path, chunk_store=chunk_store, synchronizer=
        synchronizer, cache_metadata=cache_metadata, cache_attrs=
        cache_attrs, read_only=read_only)
    return z