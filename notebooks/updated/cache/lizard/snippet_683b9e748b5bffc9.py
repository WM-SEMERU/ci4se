def _configured_socket(address, options):
    sock = _create_connection(address, options)
    ssl_context = options.ssl_context
    if ssl_context is not None:
        host = address[0]
        try:
            if _HAVE_SNI and (not is_ip_address(host) or _PY37PLUS):
                sock = ssl_context.wrap_socket(sock, server_hostname=host)
            else:
                sock = ssl_context.wrap_socket(sock)
        except _SSLCertificateError:
            sock.close()
            raise
        except IOError as exc:
            sock.close()
            _raise_connection_failure(address, exc, 'SSL handshake failed: ')
        if ssl_context.verify_mode and not getattr(ssl_context,
            'check_hostname', False) and options.ssl_match_hostname:
            try:
                match_hostname(sock.getpeercert(), hostname=host)
            except CertificateError:
                sock.close()
                raise
    sock.settimeout(options.socket_timeout)
    return sock