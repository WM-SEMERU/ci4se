def create_tls_context(self):
    tls_context = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
    if self.tls_certificate_file:
        tls_context.load_cert_chain(self.tls_certificate_file, self.
            tls_certificate_keyfile, password=self.tls_certificate_password)
    for opt in ['NO_SSLv2', 'NO_SSLv3', 'NO_COMPRESSION', 'NO_TICKET']:
        if hasattr(ssl, 'OP_' + opt):
            tls_context.options |= getattr(ssl, 'OP_' + opt)
    if self.tls_verify:
        tls_context.set_servername_callback(self.verify_tls)
        tls_context.set_default_verify_paths()
        if sys.platform in DEFAULT_CA_PATHS and path.isdir(DEFAULT_CA_PATHS
            [sys.platform]):
            tls_context.load_verify_locations(capath=DEFAULT_CA_PATHS[sys.
                platform])
        tls_context.verify_mode = ssl.CERT_REQUIRED
        tls_context.verify_flags = ssl.VERIFY_CRL_CHECK_CHAIN
    return tls_context