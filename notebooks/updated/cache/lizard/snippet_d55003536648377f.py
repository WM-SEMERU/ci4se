def generate_certificate(self, common_name, public_key_algorithm='rsa',
    signature_algorithm='rsa_sha_512', key_length=2048, signing_ca=None):
    return GatewayCertificate._create(self, common_name,
        public_key_algorithm, signature_algorithm, key_length, signing_ca)