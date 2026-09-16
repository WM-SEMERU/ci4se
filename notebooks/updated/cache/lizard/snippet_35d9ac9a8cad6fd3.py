def get_public_key_pem(cert_obj):
    return cert_obj.public_key().public_bytes(encoding=cryptography.hazmat.
        primitives.serialization.Encoding.PEM, format=cryptography.hazmat.
        primitives.serialization.PublicFormat.PKCS1)