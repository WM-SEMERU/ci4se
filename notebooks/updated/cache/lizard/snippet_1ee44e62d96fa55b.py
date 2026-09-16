def _ssl_agent(self):
    certfile = self.lookup(self.profile, 'cert')
    certfile = os.path.expanduser(certfile)
    with open(certfile) as certfp:
        pemdata = certfp.read()
        client_cert = PrivateCertificate.loadPEM(pemdata)
    trustRoot = None
    servercafile = self.lookup(self.profile, 'serverca')
    if servercafile:
        servercafile = os.path.expanduser(servercafile)
        trustRoot = RootCATrustRoot(servercafile)
    policy = ClientCertPolicy(trustRoot=trustRoot, client_cert=client_cert)
    return Agent(reactor, policy)