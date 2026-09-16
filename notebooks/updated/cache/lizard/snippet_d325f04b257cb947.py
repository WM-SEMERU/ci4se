def verifyCertificate(self, name):
    certPath = os.path.join(self.basePath, self.DIR_CERTS, '%s.cert.pem' % name
        )
    if not os.path.isfile(certPath):
        raise ValueError('Certificate [%s] not found' % certPath)
    if subprocess.call(['openssl', 'x509', '-noout', '-text', '-in', certPath]
        ) != 0:
        raise ValueError('Failed to verify the certificate')