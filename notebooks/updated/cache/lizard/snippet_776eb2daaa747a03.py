def encode_refresh_token(identity, secret, algorithm, expires_delta,
    user_claims, csrf, identity_claim_key, user_claims_key, json_encoder=None):
    token_data = {identity_claim_key: identity, 'type': 'refresh'}
    if user_claims:
        token_data[user_claims_key] = user_claims
    if csrf:
        token_data['csrf'] = _create_csrf_token()
    return _encode_jwt(token_data, expires_delta, secret, algorithm,
        json_encoder=json_encoder)