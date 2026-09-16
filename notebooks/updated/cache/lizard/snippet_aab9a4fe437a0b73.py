def server_call(method, server, timeout=DEFAULT_TIMEOUT, verify_ssl=True,
    **parameters):
    if method is None:
        raise Exception('A method name must be specified')
    if server is None:
        raise Exception('A server (eg. my3.geotab.com) must be specified')
    parameters = process_parameters(parameters)
    return _query(server, method, parameters, timeout=timeout, verify_ssl=
        verify_ssl)