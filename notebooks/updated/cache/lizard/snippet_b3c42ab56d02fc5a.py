def modify_metadata(identifier, metadata, target=None, append=None,
    append_list=None, priority=None, access_key=None, secret_key=None,
    debug=None, request_kwargs=None, **get_item_kwargs):
    item = get_item(identifier, **get_item_kwargs)
    return item.modify_metadata(metadata, target=target, append=append,
        append_list=append_list, priority=priority, access_key=access_key,
        secret_key=secret_key, debug=debug, request_kwargs=request_kwargs)