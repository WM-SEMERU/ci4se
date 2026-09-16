def put_blob(kwargs=None, storage_conn=None, call=None):
    if call != 'function':
        raise SaltCloudSystemExit(
            'The put_blob function must be called with -f or --function.')
    if kwargs is None:
        kwargs = {}
    if 'container' not in kwargs:
        raise SaltCloudSystemExit(
            'The blob container name must be specified as "container"')
    if 'name' not in kwargs:
        raise SaltCloudSystemExit('The blob name must be specified as "name"')
    if 'blob_path' not in kwargs and 'blob_content' not in kwargs:
        raise SaltCloudSystemExit(
            'Either a path to a file needs to be passed in as "blob_path" or the contents of a blob as "blob_content."'
            )
    if not storage_conn:
        storage_conn = get_storage_conn(conn_kwargs=kwargs)
    return salt.utils.msazure.put_blob(storage_conn=storage_conn, **kwargs)