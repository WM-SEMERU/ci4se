def delete(collection_name, spec, safe, last_error_args, opts, flags=0, ctx
    =None):
    if ctx:
        return _delete_compressed(collection_name, spec, opts, flags, ctx)
    return _delete_uncompressed(collection_name, spec, safe,
        last_error_args, opts, flags)