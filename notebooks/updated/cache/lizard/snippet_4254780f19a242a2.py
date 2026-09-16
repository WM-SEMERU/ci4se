def install_client_interceptors(client_interceptors=()):
    if not _valid_args(client_interceptors):
        raise ValueError('client_interceptors argument must be a list')
    from ..http_client import ClientInterceptors
    for client_interceptor in client_interceptors:
        logging.info('Loading client interceptor %s', client_interceptor)
        interceptor_class = _load_symbol(client_interceptor)
        logging.info('Adding client interceptor %s', client_interceptor)
        ClientInterceptors.append(interceptor_class())