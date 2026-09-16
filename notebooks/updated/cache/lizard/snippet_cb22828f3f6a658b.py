def cli(env, crt, csr, icc, key, notes):
    template = {'intermediateCertificate': '', 'certificateSigningRequest':
        '', 'notes': notes}
    template['certificate'] = open(crt).read()
    template['privateKey'] = open(key).read()
    if csr:
        body = open(csr).read()
        template['certificateSigningRequest'] = body
    if icc:
        body = open(icc).read()
        template['intermediateCertificate'] = body
    manager = SoftLayer.SSLManager(env.client)
    manager.add_certificate(template)