def _ssl_context_factory(parameters):
    client_cert = None
    ca_cert = None
    key = config.conf['tls']['keyfile']
    cert = config.conf['tls']['certfile']
    ca_file = config.conf['tls']['ca_cert']
    if ca_file:
        with open(ca_file, 'rb') as fd:
            ca_cert = ssl.Certificate.loadPEM(fd.read())
    if key and cert:
        with open(key) as fd:
            client_keypair = fd.read()
        with open(cert) as fd:
            client_keypair += fd.read()
        client_cert = ssl.PrivateCertificate.loadPEM(client_keypair)
    hostname = parameters.host
    if not isinstance(hostname, six.text_type):
        hostname = hostname.decode(locale.getdefaultlocale()[1])
    try:
        context_factory = ssl.optionsForClientTLS(hostname, trustRoot=
            ca_cert or ssl.platformTrust(), clientCertificate=client_cert,
            extraCertificateOptions={'raiseMinimumTo': ssl.TLSVersion.TLSv1_2})
    except AttributeError:
        context_factory = ssl.CertificateOptions(certificate=client_cert.
            original, privateKey=client_cert.privateKey.original, caCerts=[
            ca_cert.original] or ssl.platformTrust(), verify=True,
            requireCertificate=True, verifyOnce=False, enableSessions=False)
    return context_factory