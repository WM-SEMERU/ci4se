def from_json(buffer, auto_flatten=True, raise_for_index=True):
    buffer = to_bytes(buffer)
    view_out = _ffi.new('lsm_view_t **')
    index_out = _ffi.new('lsm_index_t **')
    buffer = to_bytes(buffer)
    rv = rustcall(_lib.lsm_view_or_index_from_json, buffer, len(buffer),
        view_out, index_out)
    if rv == 1:
        return View._from_ptr(view_out[0])
    elif rv == 2:
        index = Index._from_ptr(index_out[0])
        if auto_flatten and index.can_flatten:
            return index.into_view()
        if raise_for_index:
            raise IndexedSourceMap('Unexpected source map index', index=index)
        return index
    else:
        raise AssertionError('Unknown response from C ABI (%r)' % rv)