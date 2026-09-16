def list_blobs(kwargs=None, storage_conn=None, call=None):
    if call != 'function':
        raise SaltCloudSystemExit(
            'The list_blobs function must be called with -f or --function.')
    if kwargs is None:
        kwargs = {}
    if 'container' not in kwargs:
        raise SaltCloudSystemExit(
            'An storage container name must be specified as "container"')
    if not storage_conn:
        storage_conn = get_storage_conn(conn_kwargs=kwargs)
    return salt.utils.msazure.list_blobs(storage_conn=storage_conn, **kwargs)