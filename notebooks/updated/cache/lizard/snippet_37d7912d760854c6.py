def _verify_jws(self, payload, key):
    jws = JWS.from_compact(payload)
    try:
        alg = jws.signature.combined.alg.name
    except KeyError:
        msg = 'No alg value found in header'
        raise SuspiciousOperation(msg)
    if alg != self.OIDC_RP_SIGN_ALGO:
        msg = (
            "The provider algorithm {!r} does not match the client's OIDC_RP_SIGN_ALGO."
            .format(alg))
        raise SuspiciousOperation(msg)
    if isinstance(key, six.string_types):
        jwk = JWK.load(smart_bytes(key))
    else:
        jwk = JWK.from_json(key)
    if not jws.verify(jwk):
        msg = 'JWS token verification failed.'
        raise SuspiciousOperation(msg)
    return jws.payload