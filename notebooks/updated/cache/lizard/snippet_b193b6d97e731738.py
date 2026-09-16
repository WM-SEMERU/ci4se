def vn_release(call=None, kwargs=None):
    if call != 'function':
        raise SaltCloudSystemExit(
            'The vn_reserve function must be called with -f or --function.')
    if kwargs is None:
        kwargs = {}
    vn_id = kwargs.get('vn_id', None)
    vn_name = kwargs.get('vn_name', None)
    path = kwargs.get('path', None)
    data = kwargs.get('data', None)
    if vn_id:
        if vn_name:
            log.warning(
                "Both the 'vn_id' and 'vn_name' arguments were provided. 'vn_id' will take precedence."
                )
    elif vn_name:
        vn_id = get_vn_id(kwargs={'name': vn_name})
    else:
        raise SaltCloudSystemExit(
            "The vn_release function requires a 'vn_id' or a 'vn_name' to be provided."
            )
    if data:
        if path:
            log.warning(
                "Both the 'data' and 'path' arguments were provided. 'data' will take precedence."
                )
    elif path:
        with salt.utils.files.fopen(path, mode='r') as rfh:
            data = rfh.read()
    else:
        raise SaltCloudSystemExit(
            "The vn_release function requires either 'data' or a 'path' to be provided."
            )
    server, user, password = _get_xml_rpc()
    auth = ':'.join([user, password])
    response = server.one.vn.release(auth, int(vn_id), data)
    ret = {'action': 'vn.release', 'released': response[0], 'resource_id':
        response[1], 'error_code': response[2]}
    return ret