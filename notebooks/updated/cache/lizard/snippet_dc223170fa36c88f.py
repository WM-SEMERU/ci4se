def _create_sparse_kvstore(kvstore):
    update_on_kvstore = True
    if isinstance(kvstore, kvs.KVStore):
        kv = kvstore
    elif isinstance(kvstore, str):
        kv = kvs.create(kvstore)
    else:
        raise TypeError(
            "Cannot create '%s' KVStore with row_sparse parameters. The type must be KVStore or str."
             % kvstore)
    return kv, update_on_kvstore