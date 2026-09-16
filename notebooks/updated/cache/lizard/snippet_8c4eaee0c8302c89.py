def to_zarr(dataset, store=None, mode='w-', synchronizer=None, group=None,
    encoding=None, compute=True, consolidated=False):
    if isinstance(store, Path):
        store = str(store)
    if encoding is None:
        encoding = {}
    _validate_dataset_names(dataset)
    _validate_attrs(dataset)
    zstore = backends.ZarrStore.open_group(store=store, mode=mode,
        synchronizer=synchronizer, group=group, consolidate_on_close=
        consolidated)
    writer = ArrayWriter()
    dump_to_store(dataset, zstore, writer, encoding=encoding)
    writes = writer.sync(compute=compute)
    if compute:
        _finalize_store(writes, zstore)
    else:
        import dask
        return dask.delayed(_finalize_store)(writes, zstore)
    return zstore