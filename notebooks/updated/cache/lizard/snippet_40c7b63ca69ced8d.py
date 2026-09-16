def validate_and_decode(jwt_bu64, cert_obj):
    public_key = cert_obj.public_key()
    message = '.'.join(d1_common.cert.jwt.get_bu64_tup(jwt_bu64)[:2])
    signature = d1_common.cert.jwt.get_jwt_tup(jwt_bu64)[2]
    try:
        public_key.verify(signature, message, cryptography.hazmat.
            primitives.asymmetric.padding.PKCS1v15(), cryptography.hazmat.
            primitives.hashes.SHA256())
    except cryptography.exceptions.InvalidSignature as e:
        raise Exception('Signature is invalid. error="{}"'.format(str(e)))
    return d1_common.cert.jwt.get_jwt_dict(jwt_bu64)