def load_signing_key(signing_key, crypto_backend=default_backend()):
    if isinstance(signing_key, EllipticCurvePrivateKey):
        return signing_key
    elif isinstance(signing_key, (str, unicode)):
        invalid_strings = [b'-----BEGIN PUBLIC KEY-----']
        invalid_string_matches = [(string_value in signing_key) for
            string_value in invalid_strings]
        if any(invalid_string_matches):
            raise ValueError(
                'Signing key must be a private key, not a public key.')
        if is_hex(signing_key):
            try:
                private_key_pem = ECPrivateKey(signing_key).to_pem()
            except:
                pass
            else:
                try:
                    return load_pem_private_key(private_key_pem, password=
                        None, backend=crypto_backend)
                except:
                    raise InvalidPrivateKeyError()
            try:
                return load_der_private_key(signing_key, password=None,
                    backend=crypto_backend)
            except Exception as e:
                traceback.print_exc()
                raise InvalidPrivateKeyError()
        else:
            try:
                return load_pem_private_key(signing_key, password=None,
                    backend=crypto_backend)
            except:
                raise InvalidPrivateKeyError()
    else:
        raise ValueError('Signing key must be in string or unicode format.')