def _jwt_required(realm):
    token = _jwt.request_callback()
    if token is None:
        raise JWTError('Authorization Required',
            'Request does not contain an access token', headers={
            'WWW-Authenticate': 'JWT realm="%s"' % realm})
    try:
        payload = _jwt.jwt_decode_callback(token)
    except jwt.InvalidTokenError as e:
        raise JWTError('Invalid token', str(e))
    _request_ctx_stack.top.current_identity = identity = (_jwt.
        identity_callback(payload))
    if identity is None:
        raise JWTError('Invalid JWT', 'User does not exist')