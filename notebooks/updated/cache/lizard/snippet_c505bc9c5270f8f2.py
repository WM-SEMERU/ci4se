def cli(env, identifier):
    manager = SoftLayer.SSLManager(env.client)
    certificate = manager.get_certificate(identifier)
    write_cert(certificate['commonName'] + '.crt', certificate['certificate'])
    write_cert(certificate['commonName'] + '.key', certificate['privateKey'])
    if 'intermediateCertificate' in certificate:
        write_cert(certificate['commonName'] + '.icc', certificate[
            'intermediateCertificate'])
    if 'certificateSigningRequest' in certificate:
        write_cert(certificate['commonName'] + '.csr', certificate[
            'certificateSigningRequest'])