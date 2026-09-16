def create_storage_container(kwargs=None, storage_conn=None, call=None):
    if call != 'function':
        raise SaltCloudSystemExit(
            'The create_storage_container function must be called with -f or --function.'
            )
    if not storage_conn:
        storage_conn = get_storage_conn(conn_kwargs=kwargs)
    try:
        storage_conn.create_container(container_name=kwargs['name'],
            x_ms_meta_name_values=kwargs.get('meta_name_values', None),
            x_ms_blob_public_access=kwargs.get('blob_public_access', None),
            fail_on_exist=kwargs.get('fail_on_exist', False))
        return {'Success': 'The storage container was successfully created'}
    except AzureConflictHttpError:
        raise SaltCloudSystemExit(
            'There was a conflict. This usually means that the storage container already exists.'
            )