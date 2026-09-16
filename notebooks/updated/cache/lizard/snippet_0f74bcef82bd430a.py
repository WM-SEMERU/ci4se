def consolidate_metadata(store, metadata_key='.zmetadata'):
    store = normalize_store_arg(store)

    def is_zarr_key(key):
        return key.endswith('.zarray') or key.endswith('.zgroup'
            ) or key.endswith('.zattrs')
    out = {'zarr_consolidated_format': 1, 'metadata': {key: json_loads(
        store[key]) for key in store if is_zarr_key(key)}}
    store[metadata_key] = json_dumps(out)
    return open_consolidated(store, metadata_key=metadata_key)