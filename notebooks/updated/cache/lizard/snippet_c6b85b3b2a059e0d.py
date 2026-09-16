def open_consolidated(store, metadata_key='.zmetadata', mode='r+', **kwargs):
    from .storage import ConsolidatedMetadataStore
    store = normalize_store_arg(store)
    if mode not in {'r', 'r+'}:
        raise ValueError(
            "invalid mode, expected either 'r' or 'r+'; found {!r}".format(
            mode))
    meta_store = ConsolidatedMetadataStore(store, metadata_key=metadata_key)
    return open(store=meta_store, chunk_store=store, mode=mode, **kwargs)