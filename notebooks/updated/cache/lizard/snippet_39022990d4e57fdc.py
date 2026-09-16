def _configure_tls_parameters(parameters):
    cert = config.conf['tls']['certfile']
    key = config.conf['tls']['keyfile']
    if cert and key:
        _log.info(
            'Authenticating with server using x509 (certfile: %s, keyfile: %s)'
            , cert, key)
        parameters.credentials = pika.credentials.ExternalCredentials()
    else:
        cert, key = None, None
    if SSLOptions is None:
        parameters.ssl = True
        parameters.ssl_options = {'keyfile': key, 'certfile': cert,
            'ca_certs': config.conf['tls']['ca_cert'], 'cert_reqs': ssl.
            CERT_REQUIRED, 'ssl_version': ssl.PROTOCOL_TLSv1_2}
    else:
        ssl_context = ssl.create_default_context()
        if config.conf['tls']['ca_cert']:
            try:
                ssl_context.load_verify_locations(cafile=config.conf['tls']
                    ['ca_cert'])
            except ssl.SSLError as e:
                raise ConfigurationException(
                    'The "ca_cert" setting in the "tls" section is invalid ({})'
                    .format(e))
        ssl_context.options |= ssl.OP_NO_SSLv2
        ssl_context.options |= ssl.OP_NO_SSLv3
        ssl_context.options |= ssl.OP_NO_TLSv1
        ssl_context.options |= ssl.OP_NO_TLSv1_1
        ssl_context.verify_mode = ssl.CERT_REQUIRED
        ssl_context.check_hostname = True
        if cert and key:
            try:
                ssl_context.load_cert_chain(cert, key)
            except ssl.SSLError as e:
                raise ConfigurationException(
                    'The "keyfile" setting in the "tls" section is invalid ({})'
                    .format(e))
        parameters.ssl_options = SSLOptions(ssl_context, server_hostname=
            parameters.host)