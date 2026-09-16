def upload(identifier, files, metadata=None, headers=None, access_key=None,
    secret_key=None, queue_derive=None, verbose=None, verify=None, checksum
    =None, delete=None, retries=None, retries_sleep=None, debug=None,
    request_kwargs=None, **get_item_kwargs):
    item = get_item(identifier, **get_item_kwargs)
    return item.upload(files, metadata=metadata, headers=headers,
        access_key=access_key, secret_key=secret_key, queue_derive=
        queue_derive, verbose=verbose, verify=verify, checksum=checksum,
        delete=delete, retries=retries, retries_sleep=retries_sleep, debug=
        debug, request_kwargs=request_kwargs)