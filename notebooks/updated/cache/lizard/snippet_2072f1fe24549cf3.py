def template_allocate(call=None, kwargs=None):
    if call != 'function':
        raise SaltCloudSystemExit(
            'The template_allocate function must be called with -f or --function.'
            )
    if kwargs is None:
        kwargs = {}
    path = kwargs.get('path', None)
    data = kwargs.get('data', None)
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
            "The template_allocate function requires either 'data' or a file 'path' to be provided."
            )
    server, user, password = _get_xml_rpc()
    auth = ':'.join([user, password])
    response = server.one.template.allocate(auth, data)
    ret = {'action': 'template.allocate', 'allocated': response[0],
        'template_id': response[1], 'error_code': response[2]}
    return ret