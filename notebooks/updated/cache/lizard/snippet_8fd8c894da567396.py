def _get_signing_jwk_key_set(jwt_issuer):
    key_set = KEYS()
    signing_jwk_set = settings.JWT_AUTH.get('JWT_PUBLIC_SIGNING_JWK_SET')
    if signing_jwk_set:
        key_set.load_jwks(signing_jwk_set)
    key_set.add({'key': jwt_issuer['SECRET_KEY'], 'kty': 'oct'})
    return key_set