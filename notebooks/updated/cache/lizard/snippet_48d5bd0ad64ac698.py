def _create(self, common_name, public_key_algorithm='rsa',
    signature_algorithm='rsa_sha_512', key_length=2048, signing_ca=None):
    if signing_ca is None:
        signing_ca = VPNCertificateCA.objects.filter('Internal RSA').first()
    cert_auth = element_resolver(signing_ca)
    return ElementCreator(GatewayCertificate, exception=CertificateError,
        href=self.internal_gateway.get_relation('generate_certificate'),
        json={'common_name': common_name, 'public_key_algorithm':
        public_key_algorithm, 'signature_algorithm': signature_algorithm,
        'public_key_length': key_length, 'certificate_authority_href':
        cert_auth})