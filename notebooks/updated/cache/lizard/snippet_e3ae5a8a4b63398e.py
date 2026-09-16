def get_jwt_claims(self, auth_token):

    def _decode_and_verify():
        jwt_claims = jwt.JWT().unpack(auth_token).payload()
        _verify_required_claims_exist(jwt_claims)
        issuer = jwt_claims['iss']
        keys = self._jwks_supplier.supply(issuer)
        try:
            return jws.JWS().verify_compact(auth_token, keys)
        except (jwkest.BadSignature, jws.NoSuitableSigningKeys, jws.
            SignerAlgError) as exception:
            raise suppliers.UnauthenticatedException(
                'Signature verification failed', exception)
    return self._cache.get_or_create(auth_token, _decode_and_verify)