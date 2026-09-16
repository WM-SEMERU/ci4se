def verify_refresh(self, request):
    if not self.allow_refresh:
        raise InvalidTokenError('Token refresh is disabled')
    token = self.get_jwt(request)
    if token is None:
        raise InvalidTokenError('Token not found')
    try:
        claims_set = self.decode_jwt(token, self.verify_expiration_on_refresh)
    except DecodeError:
        raise DecodeError('Token could not be decoded')
    except ExpiredSignatureError:
        raise ExpiredSignatureError('Token has expired')
    userid = self.get_userid(claims_set)
    if userid is None:
        raise MissingRequiredClaimError(self.userid_claim)
    if self.refresh_nonce_handler is not None:
        if 'nonce' not in claims_set:
            raise MissingRequiredClaimError('nonce')
        if self.refresh_nonce_handler(request, userid) != claims_set['nonce']:
            raise InvalidTokenError('Refresh nonce is not valid')
    if self.refresh_delta is not None:
        if 'refresh_until' not in claims_set:
            raise MissingRequiredClaimError('refresh_until')
        now = timegm(datetime.utcnow().utctimetuple())
        refresh_until = int(claims_set['refresh_until'])
        if refresh_until < now - self.leeway:
            raise ExpiredSignatureError('Refresh nonce has expired')
    return userid