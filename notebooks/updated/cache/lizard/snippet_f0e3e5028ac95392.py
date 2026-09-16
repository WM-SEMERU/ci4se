def ssl_wrap_socket(sock, keyfile=None, certfile=None, cert_reqs=None,
    ca_certs=None, server_hostname=None, ssl_version=None, ciphers=None,
    ssl_context=None):
    context = ssl_context
    if context is None:
        context = create_urllib3_context(ssl_version, cert_reqs, ciphers=
            ciphers)
    if ca_certs:
        try:
            context.load_verify_locations(ca_certs)
        except IOError as e:
            raise SSLError(e)
        except OSError as e:
            if e.errno == errno.ENOENT:
                raise SSLError(e)
            raise
    if certfile:
        context.load_cert_chain(certfile, keyfile)
    if HAS_SNI:
        return context.wrap_socket(sock, server_hostname=server_hostname)
    return context.wrap_socket(sock)